from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from zcord import enums
from zcord.caching import MessageStore, SnowflakeStore
from zcord.http import rest
from zcord.http.client import HTTPClient
from zcord.missing import MISSING
from zcord.models import (
    Channel,
    Guild,
    Message,
    User,
)

if TYPE_CHECKING:
    from zcord.gateway import Gateway
    from zcord.models import (
        Application,
        Snowflake,
        Sticker,
        StickerPack,
    )
    from zcord.models.application import _ApplicationUpdate
    from zcord.models.interaction.interaction_response import (
        _InteractionCallback,
    )
    from zcord.models.message import _MessageCreate


log = logging.getLogger(__name__)


class ConnectionState:
    _http: HTTPClient
    _gateway: Gateway | None = None
    guilds: SnowflakeStore[Guild]
    users: SnowflakeStore[User]
    channels: SnowflakeStore[Channel]
    messages: MessageStore

    def __init__(self, token: str):
        self._http = HTTPClient(token)
        self.guilds = SnowflakeStore[Guild]()
        self.users = SnowflakeStore[User]()
        self.channels = SnowflakeStore[Channel]()
        self.messages = MessageStore()

    def _update_cache(self, event: str, data: dict) -> None:
        """Update the cache stores from a gateway event payload."""
        try:
            match enums.GatewayEvent(event):
                case enums.GatewayEvent.READY:
                    self._cache_user(data["user"])
                case enums.GatewayEvent.GUILD_CREATE:
                    self._cache_guild(data)
                    self._cache_guild_channels(data)
                case enums.GatewayEvent.GUILD_UPDATE:
                    self._cache_guild(data)
                case (
                    enums.GatewayEvent.CHANNEL_CREATE
                    | enums.GatewayEvent.CHANNEL_UPDATE
                ):
                    self._cache_channel(data)
                case enums.GatewayEvent.MESSAGE_CREATE:
                    self._cache_message(data)
                case _:
                    pass
        except Exception:
            log.warning(
                "Failed to update cache for event %s", event, exc_info=True
            )

    def _cache_user(self, data: dict) -> None:
        user = User._from_payload(data)
        self.users.set(user.id, user)

    def _cache_guild(self, data: dict) -> None:
        guild = Guild._from_payload(data)
        self.guilds.set(guild.id, guild)

    def _cache_guild_channels(self, data: dict) -> None:
        for raw_channel in data.get("channels", []):
            self._cache_channel(raw_channel)

    def _cache_channel(self, data: dict) -> None:
        channel = Channel._from_payload(data)
        if channel.id is MISSING:
            raise RuntimeError("Failed to cache a channel with no ID")
        self.channels.set(channel.id, channel)

    def _cache_message(self, data: dict) -> None:
        message = Message._from_payload(data)
        if message.id is MISSING or message.channel_id is MISSING:
            raise RuntimeError(
                "Failed to cache a message with no ID or with no channel_id"
            )
        self.messages.set(message.channel_id, message.id, message)
        if message.author is not MISSING:
            self.users.set(message.author.id, message.author)

    async def send_message(
        self,
        *,
        channel_id: int | Snowflake | Channel,
        message: Message,
        params: _MessageCreate,
    ) -> Message:
        return await rest.send_message(
            self._http, channel_id=channel_id, message=message, params=params
        )

    async def fetch_guild(
        self,
        guild_id: int | Snowflake,
        *,
        with_counts: bool | MISSING = MISSING,
    ) -> Guild:
        return await rest.fetch_guild(
            self._http, guild_id, with_counts=with_counts
        )

    async def fetch_channel_messages(
        self,
        channel_id: int | Snowflake,
        *,
        around: int | Snowflake | MISSING = MISSING,
        before: int | Snowflake | MISSING = MISSING,
        after: int | Snowflake | MISSING = MISSING,
        limit: int = 50,
    ) -> list[Message]:
        return await rest.fetch_channel_messages(
            self._http,
            channel_id,
            around=around,
            before=before,
            after=after,
            limit=limit,
        )

    async def fetch_channel_message(
        self,
        *,
        channel_id: int | Snowflake,
        message_id: int | Snowflake,
    ) -> Message:
        return await rest.fetch_channel_message(
            self._http, channel_id=channel_id, message_id=message_id
        )

    async def fetch_sticker(self, *, sticker_id: int | Snowflake) -> Sticker:
        return await rest.fetch_sticker(self._http, sticker_id=sticker_id)

    async def fetch_sticker_packs(self) -> list[StickerPack]:
        return await rest.fetch_sticker_packs(self._http)

    async def fetch_sticker_pack(
        self, *, pack_id: int | Snowflake
    ) -> StickerPack:
        return await rest.fetch_sticker_pack(self._http, pack_id=pack_id)

    async def fetch_guild_stickers(
        self, *, guild_id: int | Snowflake | Guild
    ) -> list[Sticker]:
        return await rest.fetch_guild_stickers(self._http, guild_id=guild_id)

    async def fetch_guild_sticker(
        self, *, guild_id: int | Snowflake | Guild, sticker_id: int | Snowflake
    ) -> Sticker:
        return await rest.fetch_guild_sticker(
            self._http, guild_id=guild_id, sticker_id=sticker_id
        )

    async def create_guild_sticker(
        self,
        *,
        guild_id: int | Snowflake | Guild,
        name: str,
        description: str,
        tags: str,
        file,
    ) -> Sticker:
        return await rest.create_guild_sticker(
            self._http,
            guild_id=guild_id,
            name=name,
            description=description,
            tags=tags,
            file=file,
        )

    async def edit_guild_sticker(
        self,
        *,
        guild_id: int | Snowflake | Guild,
        sticker_id: int | Snowflake,
        name: str,
        description: str | None = None,
        tags: str,
    ) -> Sticker:
        return await rest.edit_guild_sticker(
            self._http,
            guild_id=guild_id,
            sticker_id=sticker_id,
            name=name,
            description=description,
            tags=tags,
        )

    async def delete_guild_sticker(
        self,
        *,
        guild_id: int | Snowflake | Guild,
        sticker_id: int | Snowflake | Sticker,
    ) -> bool:
        return await rest.delete_guild_sticker(
            self._http, guild_id=guild_id, sticker_id=sticker_id
        )

    async def fetch_answer_voters(
        self,
        *,
        channel_id: int | Snowflake | Channel,
        message_id: int | Snowflake | Message,
        answer_id: int,
        after: int | Snowflake | MISSING = MISSING,
        limit: int = 50,
    ) -> list[User]:
        return await rest.fetch_answer_voters(
            self._http,
            channel_id=channel_id,
            message_id=message_id,
            answer_id=answer_id,
            after=after,
            limit=limit,
        )

    async def end_poll(
        self,
        *,
        channel_id: int | Snowflake | Channel,
        message_id: int | Snowflake | Message,
    ) -> Message:
        return await rest.end_poll(
            self._http,
            channel_id=channel_id,
            message_id=message_id,
        )

    async def fetch_current_application(self) -> Application:
        return await rest.fetch_current_application(self._http)

    async def edit_current_application(
        self, application: _ApplicationUpdate
    ) -> Application:
        return await rest.edit_current_application(self._http, application)

    async def fetch_channel(self, channel_id: int | Snowflake) -> Channel:
        return await rest.fetch_channel(self._http, channel_id=channel_id)

    async def fetch_user(self, user_id: int | Snowflake) -> User:
        return await rest.fetch_user(self._http, user_id=user_id)

    async def fetch_current_user(self) -> User:
        return await rest.fetch_current_user(self._http)

    async def create_interaction_response(
        self,
        *,
        interaction_id: Snowflake,
        interaction_token: str,
        callback: _InteractionCallback,
        with_response: bool = False,
    ) -> Message | None:
        return await rest.create_interaction_response(
            self._http,
            interaction_id=interaction_id,
            interaction_token=interaction_token,
            callback=callback,
            with_response=with_response,
        )
