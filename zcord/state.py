from __future__ import annotations

from typing import TYPE_CHECKING

from zcord.http.client import HTTPClient
from zcord.http.rest import REST
from zcord.missing import MISSING

if TYPE_CHECKING:
    from zcord.models import (
        Application,
        Channel,
        Guild,
        Message,
        Snowflake,
        Sticker,
        StickerPack,
        User,
    )


class ConnectionState:
    _http: HTTPClient
    _channels: dict[int, Channel]
    _users: dict[int, User]

    def __init__(self, token: str):
        self._http = HTTPClient(token)

    async def send_message(
        self, *, channel_id: int | Snowflake | Channel, message: Message
    ) -> Message:
        return await REST.send_message(
            self._http, channel_id=channel_id, message=message
        )

    async def fetch_guild(
        self,
        guild_id: int | Snowflake,
        *,
        with_counts: bool | MISSING = MISSING,
    ) -> Guild:
        return await REST.fetch_guild(
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
        return await REST.fetch_channel_messages(
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
        return await REST.fetch_channel_message(
            self._http, channel_id=channel_id, message_id=message_id
        )

    async def fetch_sticker(self, *, sticker_id: int | Snowflake) -> Sticker:
        return await REST.fetch_sticker(self._http, sticker_id=sticker_id)

    async def fetch_sticker_packs(self) -> list[StickerPack]:
        return await REST.fetch_sticker_packs(self._http)

    async def fetch_sticker_pack(
        self, *, pack_id: int | Snowflake
    ) -> StickerPack:
        return await REST.fetch_sticker_pack(self._http, pack_id=pack_id)

    async def fetch_guild_stickers(
        self, *, guild_id: int | Snowflake | Guild
    ) -> list[Sticker]:
        return await REST.fetch_guild_stickers(self._http, guild_id=guild_id)

    async def fetch_guild_sticker(
        self, *, guild_id: int | Snowflake | Guild, sticker_id: int | Snowflake
    ) -> Sticker:
        return await REST.fetch_guild_sticker(
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
        return await REST.create_guild_sticker(
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
        return await REST.edit_guild_sticker(
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
        return await REST.delete_guild_sticker(
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
        return await REST.fetch_answer_voters(
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
        return await REST.end_poll(
            self._http,
            channel_id=channel_id,
            message_id=message_id,
        )

    async def fetch_current_application(self) -> Application:
        return await REST.fetch_current_application(self._http)

    async def fetch_channel(self, channel_id: int | Snowflake) -> Channel:
        return await REST.fetch_channel(self._http, channel_id=channel_id)
