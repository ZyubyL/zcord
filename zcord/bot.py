from __future__ import annotations

from zcord.models.message import Message
from zcord.state import ConnectionState


class Bot:
    """
    Represent the bot client
    """

    def __init__(self, token: str) -> None:
        """
        Params:
            token: The bot token.
        """
        self._state = ConnectionState(token)
        Message._state = self._state

    async def __aenter__(self) -> Bot:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self._state._http.close()
