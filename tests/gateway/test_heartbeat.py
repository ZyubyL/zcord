from __future__ import annotations

import asyncio

from zcord.gateway import Heartbeat

INTERVAL = 41.25
JITTER = 0.5
NO_JITTER = 0.0


class DiscordGatewayMock:
    """Mock Discord gateway heartbeat behavior"""

    def __init__(self, beats: int) -> None:
        self._beats = beats

        self.heartbeat: Heartbeat | None = None
        self.sends = 0
        self.delays: list[float] = []
        self.done = asyncio.Event()

    async def send(self) -> None:
        self.sends += 1
        assert self.heartbeat is not None
        self.heartbeat.ack()
        if self.sends == self._beats:
            self.done.set()
            raise ConnectionResetError

    async def sleep(self, delay: float) -> None:
        self.delays.append(delay)
        await asyncio.sleep(0)


class ExpiredTimeout:
    """Mock asyncio.timeout when the ACK deadline passed"""

    def __call__(self, delay: float) -> ExpiredTimeout:
        return self

    async def __aenter__(self) -> None:
        raise TimeoutError

    async def __aexit__(self, *exc: object) -> bool:
        return False


async def unexpected_timeout() -> None:
    raise AssertionError(
        "heartbeat watchdog fired while ACK were still arriving"
    )


async def test_beats_on_interval():
    gateway = DiscordGatewayMock(beats=3)
    gateway.heartbeat = Heartbeat(
        send=gateway.send,
        on_timeout=unexpected_timeout,
        rng=lambda: JITTER,
        sleep=gateway.sleep,
    )
    await gateway.heartbeat.start(INTERVAL)
    async with asyncio.timeout(1):
        await gateway.done.wait()
    await gateway.heartbeat.stop()

    assert gateway.delays == [INTERVAL * JITTER, INTERVAL, INTERVAL]


async def test_missingn_ack_watchdog():
    timed_out: list[bool] = []
    done = asyncio.Event()

    async def send() -> None:
        await asyncio.sleep(0)

    async def sleep(delay: float) -> None:
        await asyncio.sleep(0)

    async def on_timeout() -> None:
        timed_out.append(True)
        done.set()

    heartbeat = Heartbeat(
        send=send,
        on_timeout=on_timeout,
        rng=lambda: NO_JITTER,
        sleep=sleep,
        timeout=ExpiredTimeout(),
    )
    await heartbeat.start(INTERVAL)
    async with asyncio.timeout(1):
        await done.wait()
    await heartbeat.stop()

    assert timed_out == [True]
