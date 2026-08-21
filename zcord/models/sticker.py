from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.enums import StickerFormatType, StickerType
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Sticker(Model):
    """
    Represent a Discord Sticker.

    Attributes:
        id:
            The ID of the sticker.
        pack_id:
            The ID of the pack the sticker is from.
        name:
            The name of the sticker.
        description:
            The description of the sticker.
        tags:
            The tags for autocomplete/suggestion for the sticker.
        type:
            The type of the sticker.
        format_type:
            The type of sticker format.
        available:
            Whether this guild sticker can be used.
        guild_id:
            The ID of the guild that owns this sticker.
        user:
            The user who uploaded this sticker.
        sort_value:
            The standard sticker sort order within its pack.
    """

    id: Snowflake
    name: str
    format_type: StickerFormatType
    tags: str | MISSING = MISSING
    type: StickerType | MISSING = MISSING
    pack_id: Snowflake | MISSING = MISSING
    description: str | None = None
    available: bool | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    user: User | MISSING = MISSING
    sort_value: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": StickerType,
        "format_type": StickerFormatType,
        "pack_id": Snowflake,
        "guild_id": Snowflake,
        "user": User,
    }


@dataclass(frozen=True, slots=True)
class StickerPack(Model):
    """
    Represent a pack of standard stickers.

    Attributes:
        id:
            The ID of the pack.
        stickers:
            The stickers in the pack.
        name:
            The name of the pack.
        sku_id:
            The ID of the pack's SKU.
        cover_sticker_id:
            The ID of a sticker in the pack which is shown as the pack's icon.
        description:
            The description of the pack.
        banner_asset_id:
            The ID of the pack's banner image.
    """

    id: Snowflake
    stickers: tuple[Sticker, ...]
    name: str
    sku_id: Snowflake
    description: str
    cover_sticker_id: Snowflake | MISSING = MISSING
    banner_asset_id: Snowflake | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "stickers": Sticker,
        "sku_id": Snowflake,
        "cover_sticker_id": Snowflake,
        "banner_asset_id": Snowflake,
    }
