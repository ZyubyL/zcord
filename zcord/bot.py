from __future__ import annotations

import asyncio
import contextlib
import logging
from typing import TYPE_CHECKING, Any, Final, overload

import aiohttp

from zcord import enums
from zcord._logging import setup_logging
from zcord._version import __version__
from zcord.errors import HTTPError
from zcord.gateway import Gateway
from zcord.missing import MISSING
from zcord.models.application import Application, _ApplicationUpdate
from zcord.models.channel import Channel
from zcord.models.guild import Guild
from zcord.models.install_params import InstallParams
from zcord.models.interaction.interaction import Interaction
from zcord.models.message import Message
from zcord.models.user import User
from zcord.state import ConnectionState

if TYPE_CHECKING:
    from collections.abc import Callable

    from zcord import bitfields, types
    from zcord.models.base import Model
    from zcord.models.snowflake import Snowflake

__all__ = ["Bot"]

log = logging.getLogger(__name__)


class EventConverter:
    """Convert gateway event payloads to typed listener args"""

    _CREATE_MODELS: Final[dict[str, type[Model]]] = {
        enums.GatewayEvent.READY.value: User,
        enums.GatewayEvent.GUILD_CREATE.value: Guild,
        enums.GatewayEvent.MESSAGE_CREATE.value: Message,
        enums.GatewayEvent.INTERACTION_CREATE.value: Interaction,
    }

    _UPDATE_MODELS: Final[dict[str, tuple[type[Model], str]]] = {
        enums.GatewayEvent.GUILD_UPDATE.value: (Guild, "_guilds")
    }

    def __init__(self, state: ConnectionState) -> None:
        self._state = state

    def convert(self, event: str, data: Any) -> tuple[Any, ...]:
        """
        Build the listener args for a gateway event.

        Returns:
            - `(old, new)` for update events.
            - `(model,)` for converted events.
            - `(data,)` for fall through events with no registered model.

        Notes:
            `old` could be [`None`][] if the object is not cached.
            `READY` payload is unwrapped to `user`.
        """
        if data and event in self._UPDATE_MODELS:
            model, cache_attr = self._UPDATE_MODELS[event]
            old = getattr(self._state, cache_attr, {}).get(int(data["id"]))
            return old, model._from_payload(data)
        if data and event in self._CREATE_MODELS:
            payload = (
                data["user"] if event == str(enums.GatewayEvent.READY) else data
            )
            return (self._CREATE_MODELS[event]._from_payload(payload),)
        return (data,)


class EventDispatcher:
    """Route events to registered listeners"""

    def __init__(self) -> None:
        self._listeners: dict[str, list[tuple[Callable[..., Any], bool]]] = {}
        self._tasks: set[asyncio.Task] = set()

    def register(
        self, event: str, callback: Callable[..., Any], *, once: bool
    ) -> None:
        """
        Register a listener for the event.

        Params:
            once:
                Whether to remove the listener after its first fire.
        """
        self._listeners.setdefault(event, []).append((callback, once))

    def dispatch(self, event: str, args: tuple[Any, ...]) -> None:
        """
        Fire all listeners for the event with the given arguments.

        Notes:
            Listener failures are non-blocking and is logged with traceback.
        """
        listeners = self._listeners.get(event, [])
        self._listeners[event] = [
            listener for listener in listeners if not listener[1]
        ]  # keep persisten ones

        for callback, _ in listeners:
            try:
                maybe_coro = callback(*args)
            except Exception:
                log.exception("Failed to dispatch event %s", event)
                continue
            if asyncio.iscoroutine(maybe_coro):
                task = asyncio.create_task(maybe_coro)
                self._tasks.add(task)
                task.add_done_callback(self._task_done)

    def _task_done(self, task: asyncio.Task) -> None:
        self._tasks.discard(task)
        if not task.cancelled() and (e := task.exception()) is not None:
            log.error("Failed to dispatch event", exc_info=e)


class Bot:
    """Represent the bot client"""

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
        Application._state = self._state
        Interaction._state = self._state

        self._converter = EventConverter(self._state)
        self._dispatcher = EventDispatcher()

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
        log.debug("zcord version %s", __version__)
        log.debug("aiohttp version %s", aiohttp.__version__)
        done = asyncio.Event()

        async def _connect() -> None:
            try:
                await self.fetch_current_user()
            except HTTPError as e:
                log.fatal(e)
                return done.set()
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

    @overload
    def on(
        self,
        event: str | enums.GatewayEvent,
        callback: Callable[..., Any],
    ) -> None: ...
    @overload
    def on(
        self,
        event: str | enums.GatewayEvent,
    ) -> Callable[..., Any]: ...
    def on(
        self,
        event: str | enums.GatewayEvent,
        callback: Callable[..., Any] | None = None,
    ) -> Callable[..., Any] | None:
        """
        Register a persistent event listener.

        Examples:
            There are 2 ways of registering events:

            === "By passing the callback function"
                ```py
                async def callback_func(...):
                    ...

                bot.on(GatewayEvent.READY, callback_func)
                ```
            === "Using decorator"
                ```py
                @bot.on(GatewayEvent.READY)
                async def callback_func(...):
                    ...
                ```
            Notes:
                The callback function is not required to be asynchronous.

            The same goes for [`Bot.once`][zcord.Bot.once]
        """
        return self._register_event_callback(
            event=event, callback=callback, one_time=False
        )

    @overload
    def once(
        self,
        event: str | enums.GatewayEvent,
        callback: Callable[..., Any],
    ) -> None: ...
    @overload
    def once(
        self,
        event: str | enums.GatewayEvent,
    ) -> Callable[..., Any]: ...
    def once(
        self,
        event: str | enums.GatewayEvent,
        callback: Callable[..., Any] | None = None,
    ) -> Callable[..., Any] | None:
        """
        Register a one-time event listener.

        Examples:
            See [`Bot.on`][zcord.Bot.on] for examples.
        """
        return self._register_event_callback(
            event=event, callback=callback, one_time=True
        )

    def _register_event_callback(
        self,
        *,
        event: str | enums.GatewayEvent,
        callback: Callable[..., Any] | None = None,
        one_time: bool,
    ) -> Callable[..., Any] | None:
        def _decorator(cb: Callable[..., Any]) -> Callable[..., Any]:
            self._dispatcher.register(str(event), cb, once=one_time)
            return cb

        if callback is None:  # Acts as a decorator
            return _decorator
        _decorator(callback)

    def _dispatch(self, event: str, data: Any) -> None:
        args = self._converter.convert(event, data)
        self._dispatcher.dispatch(event, args)
        self._state._update_cache(event, data)

    async def fetch_current_application(self) -> Application:
        """
        Fetch info about the current application.
        """
        return await self._state.fetch_current_application()

    async def edit_current_application(
        self,
        *,
        custom_install_url: str | MISSING = MISSING,
        description: str | MISSING = MISSING,
        role_connections_verification_url: str | MISSING = MISSING,
        scopes: types.TupleOrList[str] | MISSING = MISSING,
        permissions: str | MISSING = MISSING,
        integration_types_config: dict | MISSING = MISSING,
        flags: bitfields.ApplicationFlags | MISSING = MISSING,
        # icon: Any,
        # cover_image: Any,
        interactions_endpoint_url: str | MISSING = MISSING,
        tags: types.TupleOrList[str] | MISSING = MISSING,
        event_webhooks_url: str | MISSING = MISSING,
        event_webhooks_status: enums.EventWebhookStatus | MISSING = MISSING,
        event_webhooks_types: types.TupleOrList[enums.WebhookEventType]
        | MISSING = MISSING,
    ) -> Application:
        """
        Edit the current application.

        Params:
            custom_install_url:
                Default custom authorization URL for the app, if enabled
            description:
                Description of the app
            role_connections_verification_url:
                Role connection verification URL for the app
            integration_types_config:
                Default scopes and permissions for each supported installation \
                context. Value for each key is an integration type \
                configuration object.
            flags:
                App's public flags.
            icon:
                Icon for the app (not implemented).
            cover_image:
                Default rich presence invite cover image for the app \
                (not implemented).
            interactions_endpoint_url:
                Interactions endpoint URL for the app.
            tags:
                List of tags describing the content and functionality \
                of the app (max of 20 characters per tag). Max of 5 tags.
            event_webhooks_url:
                Event webhooks URL for the app to receive webhook events.
            event_webhooks_status:
                If webhook events are enabled for the app.
            event_webhooks_types:
                List of Webhook event types to subscribe to.
            scopes:
                Scopes of the application's default install.
            permissions:
                Permissions of the application's default install.

        Notes:
            - Only the specified parameters will be updated.
            - `scopes` and `permissions` are either both specified \
            or either bot emitted. Only specify one of them will results \
            in it being ignored.
        """
        return await self._state.edit_current_application(
            _ApplicationUpdate(
                custom_install_url=custom_install_url,
                description=description,
                role_connections_verification_url=role_connections_verification_url,
                install_params=InstallParams(
                    scopes=(*scopes,), permissions=permissions
                )
                if scopes is not MISSING and permissions is not MISSING
                else MISSING,
                integration_types_config=integration_types_config,
                flags=flags,
                # icon=icon
                # cover_image=cover_image
                interactions_endpoint_url=interactions_endpoint_url,
                tags=(*tags,) if tags is not MISSING else MISSING,
                event_webhooks_url=event_webhooks_url,
                event_webhooks_status=event_webhooks_status,
                event_webhooks_types=(*event_webhooks_types,)
                if event_webhooks_types is not MISSING
                else MISSING,
            )
        )

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
