from __future__ import annotations

import asyncio
import logging
import random
import sys
import urllib.parse
import zlib
from typing import TYPE_CHECKING, Any, Final

import aiohttp
import orjson

from zcord import bitfields, enums
from zcord.enums.gateway import GatewayCloseCode, GatewayOpcode
from zcord.http.rest import REST

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
    from contextlib import AbstractAsyncContextManager

    from zcord.http import HTTPClient
    from zcord.models._gateway import _GetGatewayBotResponse

log = logging.getLogger(__name__)


class ZlibStream:
    """zlib-stream handler"""

    SUFFIX: Final = b"\x00\x00\xff\xff"

    _buffer: bytearray
    _inflator: zlib._Decompress

    def __init__(self) -> None:
        self.reset()

    @property
    def suffix_index(self) -> int:
        """
        Get the index of the suffix string in the buffer.

        Returns:
            Non-negative index, or `-1` if not found.
        """
        return self._buffer.find(self.SUFFIX)

    @property
    def end_index(self) -> int | None:
        """
        The end index of the buffer after added the suffix.

        Returns:
            `None` if the `suffix_index` was not found.
        """
        if self.suffix_index < 0:
            return None
        return self.suffix_index + len(self.SUFFIX)

    def feed(self, chunk: bytes) -> list[bytes]:
        """
        Accumulate chunk into the buffer.

        Returns:
            All complete inflated messages found in the buffer.
        """
        self._buffer.extend(chunk)
        messages: list[bytes] = []
        while (end := self.end_index) is not None:
            compressed_msg = self._buffer[:end]
            del self._buffer[:end]
            messages.append(self._decompress_message(compressed_msg))
        return messages

    def _decompress_message(self, compressed_msg: bytearray) -> bytes:
        """
        Returns:
            The inflated message.
        """
        return self._inflator.decompress(compressed_msg)

    def reset(self) -> None:
        """
        Reset inflator for new connection.
        """
        self._buffer = bytearray()
        self._inflator = zlib.decompressobj()


class Backoff:
    """Reconnection backoff logic"""

    DELAY_STEP: Final = 1.0
    DELAY_CAP: Final = 60.0
    MAX_CONNECT_FAILURES: Final = 5
    """How many times until the gateway just accept defeat"""

    def __init__(self, *, rng: Callable[[], float] = random.random) -> None:
        """
        Params:
            rng:
                Source of the random jitter added to the reconnect delay.
        """
        self._rng = rng
        self._delay = 0.0
        self._connect_failures = 0

    @property
    def reconnect_delay(self) -> float:
        """
        The delay before trying to reconnect (including jitter).
        """
        return self._delay + self._rng()

    @property
    def connect_failures(self) -> int:
        """
        Number of consecutive connection failures.
        """
        return self._connect_failures

    def record_connect_failure(self) -> bool:
        """
        Register a failed connection attempt.

        Returns:
            Whether the failure streak reached `MAX_CONNECT_FAILURES`.
        """
        self._connect_failures += 1
        return self._connect_failures >= self.MAX_CONNECT_FAILURES

    def record_connect_success(self) -> None:
        """
        If the gateway successfully connected. Clear the failure streak.
        """
        self._connect_failures = 0

    def increase_delay(self) -> None:
        """
        Increase the delay to reconnect, capped at `DELAY_CAP`.
        """
        self._delay = min(self._delay + self.DELAY_STEP, self.DELAY_CAP)

    def reset_delay(self) -> None:
        """
        Clear the reconnect delay when the gateway is sucessfully connected.
        """
        self._delay = 0.0


class Heartbeat:
    """Keep a gateway session alive"""

    def __init__(
        self,
        *,
        send: Callable[[], Awaitable[None]],
        on_timeout: Callable[[], Awaitable[None]],
        rng: Callable[[], float] = random.random,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
        timeout: Callable[
            [float], AbstractAsyncContextManager[Any]
        ] = asyncio.timeout,
    ) -> None:
        """
        Params:
            send:
                Call to send one heartbeat payload.
            on_timeout:
                What to call when the gateway missed an ACK deadline.
            rng:
                Source of the random jitter for the first beat.
            sleep:
                Source of the sleep in between heartbeats.
            timeout:
                Timeout context manager factory.
        """
        self._send = send
        self._on_timeout = on_timeout
        self._rng = rng
        self._sleep = sleep
        self._timeout = timeout

        self._interval = 0.0
        self._task: asyncio.Task[None] | None = None
        self._ack = asyncio.Event()

    async def start(self, interval: float) -> None:
        """
        Start the heartbeat task at interval (in seconds).
        """
        await self.stop()
        self._interval = interval
        self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        """
        Cancel the heartbeat task and wait for it to finish.
        """
        if self._task is None:
            return
        self._task.cancel()
        await asyncio.gather(self._task, return_exceptions=True)
        self._task = None

    def ack(self) -> None:
        """
        Record a heartbeat ACK returned from the gateway.
        """
        self._ack.set()

    async def _run(self) -> None:
        await self._sleep(self._interval * self._rng())
        await self._send()
        while True:
            try:
                await self._wait_for_ack()
            except TimeoutError:
                log.warning("Heartbeat timed out")
                await self._on_timeout()
                return
            await self._sleep(self._interval)
            await self._send()

    async def _wait_for_ack(self) -> None:
        async with self._timeout(self._interval):
            await self._ack.wait()
        self._ack.clear()


class Gateway:
    VERSION: Final = 10
    ENCODING: Final = "json"
    COMPRESSION: Final = "zlib-stream"

    def __init__(
        self,
        *,
        http: HTTPClient,
        token: str,
        intents: bitfields.Intents,
        dispatch: Callable[..., Any] | None = None,
    ) -> None:
        self._http = http
        self._token = token
        self._intents = intents
        self._dispatch = dispatch

        self._session: aiohttp.ClientWebSocketResponse | None = None
        self._gateway_response: _GetGatewayBotResponse | None = None
        self._sequence: int | None = None
        self._resume_url: str | None = None
        self._session_id: str | None = None
        self._reconnect_event = asyncio.Event()

        self._stream = ZlibStream()

        self._backoff = Backoff()

        self._heartbeat = Heartbeat(
            send=self._send_heartbeat,
            on_timeout=self._on_heartbeat_timeout,
        )

        self._closed = False

    @property
    def ws_url(self) -> str | None:
        if self._resume_url is not None:
            url = self._resume_url
        elif self._gateway_response is not None:
            url = self._gateway_response.url
        else:
            url = None
        if url is None:
            return None
        params = {
            "v": self.VERSION,
            "encoding": self.ENCODING,
            "compress": self.COMPRESSION,
        }
        return f"{url}?{urllib.parse.urlencode(params)}"

    async def _handle_connection(
        self, ws: aiohttp.ClientWebSocketResponse
    ) -> None:
        async for msg in ws:
            if msg.type in (
                aiohttp.WSMsgType.CLOSED,
                aiohttp.WSMsgType.CLOSING,
            ):
                break

            if msg.type is aiohttp.WSMsgType.BINARY:
                for message in self._stream.feed(msg.data):
                    await self._handle_ws_msg(message)
            elif msg.type is aiohttp.WSMsgType.TEXT:
                await self._handle_ws_msg(msg.data)

        await self._handle_ws_close_msg(ws.close_code)

    async def _handle_ws_close_msg(self, close_code: int | None) -> None:
        if close_code is None:
            return
        log.debug("WS was closed with code: %d", close_code)
        match close_code:
            case GatewayCloseCode.DISALLOWED_INTENTS:
                await self.close()
                log.error(
                    "You have enabled some privileged intents "
                    "that are not enabled in the Developer portal."
                )

    def _update_sequence(self, s: int | None) -> None:
        if s is not None:
            self._sequence = s

    async def _handle_ws_msg(self, data: str | bytes) -> None:
        payload = orjson.loads(data)
        op = payload["op"]
        d = payload.get("d")
        s = payload.get("s")
        self._update_sequence(s)

        match op:
            case GatewayOpcode.HELLO:
                await self._on_hello(d)
            case GatewayOpcode.HEARTBEAT_ACK:
                log.debug("Heartbeat ACK received")
                self._heartbeat.ack()
            case GatewayOpcode.HEARTBEAT:
                await self._send_heartbeat()
            case GatewayOpcode.DISPATCH:
                t = payload.get("t")
                self._on_dispatch(t, d)
            case GatewayOpcode.RECONNECT:
                log.info("Resuming connection...")
                await self._disconnect()
            case GatewayOpcode.INVALID_SESSION:
                log.info("Invalid session, reconnecting...")
                if not d:
                    self._reset_session()
                await self._disconnect()
            case _:
                log.debug("Unhandled opcode: %s", op)

    async def _on_hello(self, d: dict) -> None:
        interval = d["heartbeat_interval"] / 1000
        log.debug("Hello received, heartbeat interval: %s", interval)
        await self._heartbeat.start(interval)
        if self._session_id is not None:
            await self._send_resume()
            return
        await self._send_identify()

    def _reset_session(self) -> None:
        self._session_id = None
        self._resume_url = None
        self._sequence = None
        self._gateway_response = None

    async def _send_resume(self) -> None:
        log.debug("Sending resume...")
        await self._send(
            {
                "op": GatewayOpcode.RESUME,
                "d": {
                    "token": self._token,
                    "session_id": self._session_id,
                    "seq": self._sequence,
                },
            }
        )

    async def _send_identify(self) -> None:
        log.debug("Sending identify...")
        await self._send(
            {
                "op": GatewayOpcode.IDENTIFY,
                "d": {
                    "token": self._token,
                    "intents": self._intents,
                    "properties": {
                        "os": sys.platform,
                        "browser": "zcord",
                        "device": "zcord",
                    },
                },
            }
        )

    async def _send_heartbeat(self) -> None:
        log.debug("Sending heartbeat...")
        await self._send({"op": GatewayOpcode.HEARTBEAT, "d": self._sequence})

    def _on_dispatch(self, name: str | None, data: Any) -> None:
        log.debug("Dispatch: %s", name)
        if name == str(enums.GatewayEvent.READY):
            self._on_ready(data)
        # forward to external handlers
        if self._dispatch and name:
            self._dispatch(name, data)

    def _on_ready(self, data: dict) -> None:
        self._backoff.reset_delay()
        self._resume_url = data["resume_gateway_url"]
        self._session_id = data["session_id"]
        log.info(
            "Session ID: %s has connected to the gateway", self._session_id
        )

    async def _send(self, payload: dict) -> None:
        if self._session and not self._session.closed:
            await self._session.send_str(orjson.dumps(payload).decode())
        else:
            log.debug("Session closed while trying to send payload %s", payload)

    async def _get_gateway_bot(self) -> None:
        if not self._gateway_response:
            self._gateway_response = await REST._get_gateway_bot(self._http)

    async def connect(self) -> None:
        if self.ws_url is None:
            await self._get_gateway_bot()

        # There's no way after trying to get the ws url it's still None
        if self.ws_url is None:
            raise RuntimeError("Cannot get websocket url")

        log.debug("Websocket URL: %s", self.ws_url)
        self._stream.reset()
        try:
            async with self._http.session.ws_connect(self.ws_url) as ws:
                self._backoff.record_connect_success()
                self._session = ws
                await self._handle_connection(ws)
        except (aiohttp.ClientError, OSError) as e:
            if self._backoff.record_connect_failure():
                log.error(
                    "Failed to connect to gateway %d times in a row: %s",
                    self._backoff.connect_failures,
                    e,
                )
                raise e
            log.warning(
                "Failed to connect to gateway (%d/%d): %s",
                self._backoff.connect_failures,
                Backoff.MAX_CONNECT_FAILURES,
                e,
            )
        finally:
            self._session = None

    async def try_reconnect(self) -> None:
        if self._closed:
            return
        delay = self._backoff.reconnect_delay
        log.info("Reconnecting in %.2f seconds...", delay)
        self._reconnect_event.clear()
        try:
            async with asyncio.timeout(delay):
                await self._reconnect_event.wait()
        except TimeoutError:
            self._backoff.increase_delay()

    async def run(self) -> None:
        """
        Connect to the gateway and start the event loop.
        """
        while not self._closed:
            await self.connect()

            await self.try_reconnect()

    async def _on_heartbeat_timeout(self) -> None:
        await self._close_session(message=b"heartbeat timeout")

    async def _close_session(
        self,
        *,
        code: aiohttp.WSCloseCode = aiohttp.WSCloseCode.GOING_AWAY,
        message: bytes = b"",
    ) -> None:
        if self._session and not self._session.closed:
            log.debug("Closing gateway session (code=%s)", code)
            await self._session.close(code=code, message=message)

    async def _disconnect(
        self,
        *,
        code: aiohttp.WSCloseCode = aiohttp.WSCloseCode.GOING_AWAY,
        message: bytes = b"",
    ) -> None:
        log.debug("Gateway disconnected (code=%s)", code)
        await self._heartbeat.stop()
        await self._close_session(code=code, message=message)

    async def close(self) -> None:
        await self._disconnect(code=aiohttp.WSCloseCode.OK)
        self._closed = True
        self._reconnect_event.set()
