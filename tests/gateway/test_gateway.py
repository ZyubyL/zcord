from __future__ import annotations

import sys

import aiohttp
import orjson
import pytest

from zcord import bitfields, enums
from zcord.enums.gateway import GatewayOpcode
from zcord.gateway import Backoff, Gateway
from zcord.http import HTTPClient

from .test_zlib import DiscordWireMock

TOKEN = "mock.token"
INTENTS = bitfields.Intents(0)
RESUME_URL = "wss://resume.test/"

HELLO = orjson.dumps(
    {"op": GatewayOpcode.HELLO, "d": {"heartbeat_interval": 41250}}
)
READY = orjson.dumps(
    {
        "op": GatewayOpcode.DISPATCH,
        "t": str(enums.GatewayEvent.READY),
        "s": 1,
        "d": {
            "session_id": "abc",
            "resume_gateway_url": RESUME_URL,
        },
    }
)
INVALID_SESSION = orjson.dumps(
    {
        "op": GatewayOpcode.INVALID_SESSION,
        "d": False,
    }
)

IDENTIFY = {
    "op": GatewayOpcode.IDENTIFY,
    "d": {
        "token": TOKEN,
        "intents": INTENTS,
        "properties": {
            "os": sys.platform,
            "browser": "zcord",
            "device": "zcord",
        },
    },
}
RESUME = {
    "op": GatewayOpcode.RESUME,
    "d": {
        "token": TOKEN,
        "session_id": "abc",
        "seq": 1,
    },
}


def ws_url(base: str) -> str:
    return (
        f"{base}?v={Gateway.VERSION}"
        f"&encoding={Gateway.ENCODING}&compress={Gateway.COMPRESSION}"
    )


class WSSMock:
    """Mock websocket"""

    def __init__(self, frames: list[aiohttp.WSMessage]) -> None:
        self._frames = frames

        self.sent: list[dict] = []
        self.closed = False
        self.close_code: int | None = None

    def __aiter__(self) -> WSSMock:
        self._iter = iter(self._frames)
        return self

    async def __anext__(self) -> aiohttp.WSMessage:
        try:
            return next(self._iter)
        except StopIteration:
            raise StopAsyncIteration from None

    async def __aenter__(self) -> WSSMock:
        return self

    async def __aexit__(self, *exc: object) -> bool:
        return False

    async def send_str(self, data: str) -> None:
        self.sent.append(orjson.loads(data))

    async def close(self, *, code: object = None, message: bytes = b"") -> None:
        self.closed = True


class ClientSessionMock:
    """Mock aiohttp.ClientSession"""

    def __init__(self, sockets: list[WSSMock]) -> None:
        self._sockets = iter(sockets)

        self.urls: list[str] = []

    def ws_connect(self, url: str) -> WSSMock:
        self.urls.append(url)
        return next(self._sockets)


class FailSessionMock:
    """Mock session on dead network"""

    def __init__(self) -> None:
        self.attempts = 0

    def ws_connect(self, url: str) -> WSSMock:
        self.attempts += 1
        raise aiohttp.ClientError("connection refused")


def frames(
    gateway: DiscordWireMock, *messages: bytes
) -> list[aiohttp.WSMessage]:
    """Mock frames as received"""
    return [
        aiohttp.WSMessage(aiohttp.WSMsgType.BINARY, gateway.send(message), None)
        for message in messages
    ]


def make_gateway(session: ClientSessionMock | FailSessionMock) -> Gateway:
    return Gateway(
        http=HTTPClient(TOKEN),
        token=TOKEN,
        intents=INTENTS,
        backoff=Backoff(rng=lambda: 0.0),
        ws_connect=session.ws_connect,
    )


@pytest.mark.parametrize(
    ("first_frames", "expected_sent", "expected_urls"),
    [
        (
            [HELLO, READY],
            RESUME,
            [ws_url(Gateway.DEFAULT_WS_URL), ws_url(RESUME_URL)],
        ),
        (
            [HELLO, READY, INVALID_SESSION],
            IDENTIFY,
            [ws_url(Gateway.DEFAULT_WS_URL), ws_url(Gateway.DEFAULT_WS_URL)],
        ),
    ],
    ids=(
        "resume-session",
        "reidentifies-after-invalid-session",
    ),
)
async def test_second_connection(first_frames, expected_sent, expected_urls):
    first = WSSMock(frames(DiscordWireMock(), *first_frames))
    second = WSSMock(frames(DiscordWireMock(), HELLO))
    session = ClientSessionMock([first, second])
    gateway = make_gateway(session)

    await gateway.connect()
    await gateway.connect()
    await gateway.close()

    assert first.sent == [IDENTIFY]
    assert second.sent == [expected_sent]
    assert session.urls == expected_urls


async def test_give_up_after_max_failures():
    session = FailSessionMock()
    gateway = make_gateway(session)

    with pytest.raises(aiohttp.ClientError):
        for _ in range(Backoff.MAX_CONNECT_FAILURES):
            await gateway.connect()
    await gateway.close()

    assert session.attempts == Backoff.MAX_CONNECT_FAILURES
