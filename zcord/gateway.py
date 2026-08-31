from __future__ import annotations

import asyncio
import contextlib
import logging
import random
import sys
from typing import TYPE_CHECKING, Any

import aiohttp
import orjson

from zcord import bitfields, enums
from zcord.enums.gateway import GatewayCloseCode, GatewayOpcode
from zcord.http.rest import REST

if TYPE_CHECKING:
    from collections.abc import Callable

    from zcord.http import HTTPClient
    from zcord.models._gateway import _GetGatewayBotResponse

log = logging.getLogger(__name__)


class Gateway:
    VERSION = 10
    ENCODING = "json"

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
        self._sequence: int | None = None
        self._heartbeat_interval: float = 0
        self._heartbeat_task: asyncio.Task[None] | None = None
        self._heartbeat_ack = asyncio.Event()
        self._heartbeat_timeout = asyncio.Event()
        self._resume_url: str | None = None
        self._session_id: str | None = None
        self._reconnect_event = asyncio.Event()

        self._gateway_response: _GetGatewayBotResponse | None = None

        self._backoff = 0.0  # Reconnect backoff
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
        return f"{url}?v={self.VERSION}&encoding={self.ENCODING}"

    async def _handle_connection(
        self, ws: aiohttp.ClientWebSocketResponse
    ) -> None:
        async for msg in ws:
            if msg.type in (
                aiohttp.WSMsgType.CLOSED,
                aiohttp.WSMsgType.CLOSING,
            ):
                break

            if msg.type != aiohttp.WSMsgType.TEXT:
                continue

            await self._handle_ws_msg(msg)

        self._heartbeat_timeout.clear()
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

    async def _handle_ws_msg(self, msg: aiohttp.WSMessage) -> None:
        payload = orjson.loads(msg.data)
        op = payload["op"]
        d = payload.get("d")
        s = payload.get("s")
        self._update_sequence(s)

        match op:
            case GatewayOpcode.HELLO:
                await self._on_hello(d)
            case GatewayOpcode.HEARTBEAT_ACK:
                log.debug("Heartbeat ACK received")
                self._heartbeat_ack.set()
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
        self._heartbeat_interval = d["heartbeat_interval"] / 1000
        log.debug(
            "Hello received, heartbeat interval: %s",
            self._heartbeat_interval,
        )
        self._cancel_heartbeat_task(renew=True)
        if self._session_id is not None:
            await self._send_resume()
            return
        await self._send_identify()

    def _reset_session(self) -> None:
        self._session_id = None
        self._resume_url = None
        self._sequence = None
        self._gateway_response = None

    def _cancel_heartbeat_task(self, renew: bool = False) -> None:
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
        if renew:
            self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())

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

    async def _first_heartbeat(self) -> None:
        jitter = random.random()
        await asyncio.sleep(self._heartbeat_interval * jitter)
        if self._closed:
            return
        await self._send_heartbeat()

    async def _wait_for_heartbeat_ack(self) -> None:
        await asyncio.wait_for(
            self._heartbeat_ack.wait(), timeout=self._heartbeat_interval
        )
        self._heartbeat_ack.clear()

    async def _heartbeat_loop(self) -> None:
        await self._first_heartbeat()

        while not self._closed:
            try:
                await self._wait_for_heartbeat_ack()
            except TimeoutError:
                log.warning("Heart beat timed out")
                self._heartbeat_timeout.set()
                await self._close_session(message=b"heartbeat timeout")
                return

            await asyncio.sleep(self._heartbeat_interval)
            await self._send_heartbeat()

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
        self._backoff = 0.0
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
        try:
            async with (
                aiohttp.ClientSession() as session,
                session.ws_connect(self.ws_url) as ws,
            ):
                self._session = ws
                await self._handle_connection(ws)
        except (aiohttp.ClientError, OSError) as e:
            log.warning("Failed to connect to gateway: %s", e)
        finally:
            self._session = None

    @property
    def reconnect_delay(self) -> float:
        return self._backoff + random.random()

    async def try_reconnect(self) -> None:
        if self._closed:
            return
        log.info("Reconnecting in %.2f seconds...", self.reconnect_delay)
        self._reconnect_event.clear()
        with contextlib.suppress(TimeoutError):
            await asyncio.wait_for(
                self._reconnect_event.wait(), timeout=self.reconnect_delay
            )
        self._increase_backoff()

    def _increase_backoff(self) -> None:
        self._backoff = min(self._backoff + 1.0, 60.0)

    async def run(self) -> None:
        """
        Connect to the gateway and start the event loop.
        """
        while not self._closed:
            await self.connect()

            await self.try_reconnect()

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
        self._heartbeat_timeout.clear()
        self._cancel_heartbeat_task()
        await self._close_session(code=code, message=message)

    async def close(self) -> None:
        await self._disconnect(code=aiohttp.WSCloseCode.OK)
        self._closed = True
        self._reconnect_event.set()
