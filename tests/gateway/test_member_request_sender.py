from __future__ import annotations

import asyncio

from zcord.gateway import MemberRequestSender

GUILD_IDS = (1, 2, 3)
INTERVAL = MemberRequestSender.SEND_INTERVAL


class GatewayMock:
    """Mock gateway recording sent member requests"""

    def __init__(self, guild_ids: tuple[int, ...]) -> None:
        self._guild_ids = guild_ids

        self.sent: list[int] = []
        self.delays: list[float] = []
        self.done = asyncio.Event()

    async def send(self, guild_id: int) -> None:
        self.sent.append(guild_id)
        if self.sent == list(self._guild_ids):
            self.done.set()

    async def sleep(self, delay: float) -> None:
        self.delays.append(delay)
        await asyncio.sleep(0)


async def test_sends_paced_requests():
    gateway = GatewayMock(GUILD_IDS)
    sender = MemberRequestSender(send=gateway.send, sleep=gateway.sleep)

    await sender.start()

    for guild_id in GUILD_IDS:
        sender.enqueue(guild_id)

    async with asyncio.timeout(1):
        await gateway.done.wait()

    await sender.stop()

    assert gateway.sent == list(GUILD_IDS)
    assert gateway.delays == [INTERVAL] * len(GUILD_IDS)
