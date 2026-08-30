from __future__ import annotations

import asyncio
import contextlib
import logging
from importlib.metadata import version
from typing import TYPE_CHECKING, Any

import aiohttp

from zcord import enums
from zcord._logging import setup_logging
from zcord.gateway import Gateway
from zcord.models.channel import Channel
from zcord.models.guild import Guild
from zcord.models.message import Message
from zcord.state import ConnectionState

if TYPE_CHECKING:
    from collections.abc import Callable

    from zcord import bitfields
    from zcord.models.application import Application
    from zcord.models.base import Model
    from zcord.models.snowflake import Snowflake
    from zcord.models.user import User

log = logging.getLogger(__name__)

_EVENT_MODELS: dict[str, type[Model]] = {
    enums.GatewayEvent.GUILD_CREATE.value: Guild,
    enums.GatewayEvent.MESSAGE_CREATE.value: Message,
}

_UPDATE_EVENTS: dict[str, tuple[type[Model], str]] = {
    enums.GatewayEvent.GUILD_UPDATE.value: (Guild, "_guilds")
}


class Bot:
    """
    Represent the bot client
    """

    def __init__(
        self, token: str, *, intents: bitfields.Intents | None
    ) -> None:
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
        if intents is not None:
            self._state._gateway = Gateway(
                http=self._state._http,
                token=token,
                intents=intents,
                dispatch=self._dispatch,
            )
        else:
            log.warning(
                "No intents provided, bot will only perform HTTP requests."
            )
        Message._state = self._state
        Channel._state = self._state

        self._events: dict[str, list[tuple[Callable[..., Any], bool]]] = {}
        self._tasks: set[asyncio.Task] = set()

    async def __aenter__(self) -> Bot:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()

    async def close(self) -> None:
        log.info("Closing...")
        if self._state._gateway:
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
            if self._state._gateway is not None:
                try:
                    await self._state._gateway.run()
                finally:
                    done.set()

        task = asyncio.create_task(_connect())
        with contextlib.suppress(KeyboardInterrupt):
            await done.wait()
        task.cancel()

    def run(self) -> None:
        """
        Run the bot loop.
        """
        if not logging.getLogger("zcord").handlers:
            setup_logging()

        async def _main() -> None:
            try:
                await self.start()
            finally:
                await self.close()

        try:
            import uvloop

            log.debug("uvloop version %s", uvloop.__version__)
            uvloop.run(_main())
        except ImportError:
            asyncio.run(_main())
        except KeyboardInterrupt:
            pass

    def on(
        self, event: str | enums.GatewayEvent, callback: Callable[..., Any]
    ) -> None:
        """
        Register a persistent event listener.
        """
        self._events.setdefault(str(event), []).append((callback, False))

    def once(
        self, event: str | enums.GatewayEvent, callback: Callable[..., Any]
    ) -> None:
        """
        Register a one-time event listener.
        """
        self._events.setdefault(str(event), []).append((callback, True))

    def _dispatch(self, event: str, *args: Any) -> None:
        """
        Dispatch an event to all registered listeners.
        """
        listeners = self._events.get(event, [])
        self._events[event] = [
            callback for callback in listeners if not callback[1]
        ]  # keep persistent listeners
        for callback, _ in listeners:
            data = args[0] if args else None
            # Update event will have 2 args: old and new
            if data and event in _UPDATE_EVENTS:
                model, cache_attr = _UPDATE_EVENTS[event]
                obj_id = int(data["id"])
                old = getattr(self._state, cache_attr, {}).get(obj_id)
                new = model._from_payload(data)
                try:
                    maybe_coro = callback(old, new)
                except Exception:
                    log.exception("Failed to dispatch event %s", event)
                    continue
            # Some other events will have 1 arg: the object
            elif data and event in _EVENT_MODELS:
                try:
                    maybe_coro = callback(
                        _EVENT_MODELS[event]._from_payload(data)
                    )
                except Exception:
                    log.exception("Failed to dispatch event %s", event)
                    continue
            else:
                try:
                    maybe_coro = callback(*args) if args else callback()
                except Exception:
                    log.exception("Failed to dispatch event %s", event)
                    continue
            if asyncio.iscoroutine(maybe_coro):
                task = asyncio.create_task(maybe_coro)
                self._tasks.add(task)
                task.add_done_callback(self._tasks.discard)

        if args:
            self._state._update_cache(event, args[0])

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
