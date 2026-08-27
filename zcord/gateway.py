from __future__ import annotations

import asyncio
import logging
import random
import sys
from typing import TYPE_CHECKING, Any

import aiohttp
import orjson

from zcord import bitfields, enums

if TYPE_CHECKING:
    from zcord.http import HTTPClient

log = logging.getLogger(__name__)


class Gateway:
    VERSION = 10
    ENCODING = "json"

    def __init__(
        self, *, http: HTTPClient, token: str, intents: bitfields.Intents
    ) -> None:
        self._http = http
        self._token = token
        self._intents = intents

        self._session: aiohttp.ClientWebSocketResponse | None = None
        self._sequence: int | None = None
        self._heartbeat_interval: float = 0
        self._heartbeat_task: asyncio.Task[None] | None = None
        self._heartbeat_ack = asyncio.Event()
        self._resume_url: str | None = None
        self._session_id: str | None = None

        self._closed = False

    async def _get_wss_url(self) -> str:
        _, data = await self._http.request("GET", "/gateway/bot")
        assert isinstance(data, dict)
        return data["url"]

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
            payload = orjson.loads(msg.data)
            op = payload["op"]
            d = payload.get("d")
            s = payload.get("s")
            if s is not None:
                self._sequence = s
            match op:
                case enums.GatewayOpcode.HELLO:
                    await self._on_hello(d)
                case enums.GatewayOpcode.HEARTBEAT_ACK:
                    log.debug("Heartbeat ACK received")
                    self._heartbeat_ack.set()
                case enums.GatewayOpcode.HEARTBEAT:
                    await self._send_heartbeat()
                case enums.GatewayOpcode.DISPATCH:
                    t = payload.get("t")
                    self._on_dispatch(t, d)

    async def _on_hello(self, d: dict) -> None:
        self._heartbeat_interval = d["heartbeat_interval"] / 1000
        log.debug(
            "Hello received, heartbeat interval: %s",
            self._heartbeat_interval,
        )
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        await self._identify()

    async def _identify(self) -> None:
        log.debug("Sending identify")
        await self._send(
            {
                "op": enums.GatewayOpcode.IDENTIFY,
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

    async def _heartbeat_loop(self) -> None:
        jitter = random.random()
        await asyncio.sleep(self._heartbeat_interval * jitter)
        await self._send_heartbeat()

        while not self._closed:
            try:
                await asyncio.wait_for(
                    self._heartbeat_ack.wait(), timeout=self._heartbeat_interval
                )
                self._heartbeat_ack.clear()
            except TimeoutError:
                if self._session and not self._session.closed:
                    await self._session.close(
                        code=aiohttp.WSCloseCode.GOING_AWAY,
                        message=b"heartbeat timeout",
                    )
                return
            await asyncio.sleep(self._heartbeat_interval)
            await self._send_heartbeat()

    async def _send_heartbeat(self) -> None:
        await self._send(
            {"op": enums.GatewayOpcode.HEARTBEAT, "d": self._sequence}
        )
        log.debug("Sent heartbeat")

    def _on_dispatch(self, name: str | None, data: Any) -> None:
        if name == "READY":
            self._on_ready(data)

    def _on_ready(self, data: dict) -> None:
        log.info("Gateway ready")
        self._resume_url = data.get("resume_gateway_url")
        self._session_id = data.get("session_id")

    async def _send(self, payload: dict) -> None:
        if self._session and not self._session.closed:
            await self._session.send_str(orjson.dumps(payload).decode())

    async def run(self) -> None:
        """
        Connect to the gateway and start the event loop.
        """
        wss_url = await self._get_wss_url()
        url = f"{wss_url}?v={self.VERSION}&encoding={self.ENCODING}"

        log.info("Connecting to gateway...")
        async with (
            aiohttp.ClientSession() as session,
            session.ws_connect(url) as ws,
        ):
            self._session = ws
            try:
                await self._handle_connection(ws)
            finally:
                self._session = None

    async def close(self) -> None:
        self._closed = True
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
        if self._session and not self._session.closed:
            await self._session.close(
                code=aiohttp.WSCloseCode.OK,
                message=b"",
            )
