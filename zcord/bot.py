from __future__ import annotations

import asyncio
import contextlib
import logging
from importlib.metadata import version
from typing import TYPE_CHECKING

import aiohttp

from zcord.gateway import Gateway
from zcord.models.channel import Channel
from zcord.models.message import Message
from zcord.state import ConnectionState

if TYPE_CHECKING:
    from zcord import bitfields
    from zcord.models.application import Application
    from zcord.models.guild import Guild
    from zcord.models.snowflake import Snowflake
    from zcord.models.user import User

log = logging.getLogger(__name__)


class Bot:
    """
    Represent the bot client
    """

    def __init__(self, token: str, *, intents: bitfields.Intents) -> None:
        """
        Params:
            token:
                The bot token.
            intents:
                The intents to use for gateway connection.

                Notes:
                    If you don't provide intents, the bot can only perform \
                    HTTP requests.
        """
        self._state = ConnectionState(token)
        self._state._gateway = Gateway(
            http=self._state._http, token=token, intents=intents
        )
        Message._state = self._state
        Channel._state = self._state

    async def __aenter__(self) -> Bot:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        log.info("Closing...")
        await self._state._gateway.close()
        await self._state._http.close()

    async def start(self) -> None:
        """
        Start the bot loop.
        """
        log.debug("zcord version %s", version("zcord"))
        log.debug("aiohttp version %s", aiohttp.__version__)
        done = asyncio.Event()

        async def _connect() -> None:
            await self._state._gateway.run()
            done.set()

        task = asyncio.create_task(_connect())
        with contextlib.suppress(KeyboardInterrupt):
            await done.wait()
        task.cancel()

    async def fetch_current_application(self) -> Application:
        """
        Fetch info about the current application.
        """
        return await self._state.fetch_current_application()

    async def fetch_channel(self, channel_id: int | Snowflake) -> Channel:
        """
        Fetch a channel by its ID.
        """
        return await self._state.fetch_channel(channel_id)

    async def fetch_guild(self, guild_id: int | Snowflake) -> Guild:
        """
        Fetch a guild by its ID.
        """
        return await self._state.fetch_guild(guild_id)

    async def fetch_user(self, user_id: int | Snowflake) -> User:
        """
        Fetch a user by their ID.
        """
        return await self._state.fetch_user(user_id)

    async def fetch_current_user(self) -> User:
        """
        Fetch the current bot user.
        """
        return await self._state.fetch_current_user()

    async def fetch_message(
        self, *, channel_id: int | Snowflake, message_id: int | Snowflake
    ) -> Message:
        """
        Fetch a message by its ID and channel ID.
        """
        return await self._state.fetch_channel_message(
            channel_id=channel_id, message_id=message_id
        )
