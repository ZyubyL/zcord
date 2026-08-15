from __future__ import annotations

from typing import TYPE_CHECKING

from zcord.models.channel import Channel
from zcord.models.message import Message
from zcord.state import ConnectionState

if TYPE_CHECKING:
    from zcord.models.application import Application
    from zcord.models.guild import Guild
    from zcord.models.snowflake import Snowflake
    from zcord.models.user import User


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
        Channel._state = self._state

    async def __aenter__(self) -> Bot:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        await self._state._http.close()

    async def fetch_current_application(self) -> Application:
        """*|coro|*

        Fetch info about the current application.
        """
        return await self._state.fetch_current_application()

    async def fetch_channel(self, channel_id: int | Snowflake) -> Channel:
        """*|coro|*

        Fetch a channel by its ID.
        """
        return await self._state.fetch_channel(channel_id)

    async def fetch_guild(self, guild_id: int | Snowflake) -> Guild:
        """*|coro|*

        Fetch a guild by its ID.
        """
        return await self._state.fetch_guild(guild_id)

    async def fetch_user(self, user_id: int | Snowflake) -> User:
        """*|coro|*

        Fetch a user by their ID.
        """
        return await self._state.fetch_user(user_id)

    async def fetch_current_user(self) -> User:
        """*|coro|*

        Fetch the current bot user.
        """
        return await self._state.fetch_current_user()

    async def fetch_message(
        self, *, channel_id: int | Snowflake, message_id: int | Snowflake
    ) -> Message:
        """*|coro|*

        Fetch a message by its ID and channel ID.
        """
        return await self._state.fetch_channel_message(
            channel_id=channel_id, message_id=message_id
        )
