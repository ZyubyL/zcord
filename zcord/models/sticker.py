from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Sticker(Model):
    """
    Represent a Discord Sticker.
    """

    id: Snowflake
    """
    The ID of the sticker.
    """

    name: str
    """
    The name of the sticker.
    """

    format_type: enums.StickerFormatType
    """
    The type of sticker format.
    """

    tags: str | MISSING = MISSING
    """
    The tags for autocomplete/suggestion for the sticker.
    """

    type: enums.StickerType | MISSING = MISSING
    """
    The type of the sticker.
    """

    pack_id: Snowflake | MISSING = MISSING
    """
    The ID of the pack the sticker is from.
    """

    description: str | None = None
    """
    The description of the sticker.
    """

    available: bool | MISSING = MISSING
    """
    Whether this guild sticker can be used.
    """

    guild_id: Snowflake | MISSING = MISSING
    """
    The ID of the guild that owns this sticker.
    """

    user: User | MISSING = MISSING
    """
    The user who uploaded this sticker.
    """

    sort_value: int | MISSING = MISSING
    """
    The standard sticker sort order within its pack.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": enums.StickerType,
        "format_type": enums.StickerFormatType,
        "pack_id": Snowflake,
        "guild_id": Snowflake,
        "user": User,
    }


@dataclass(frozen=True, slots=True)
class StickerPack(Model):
    """
    Represent a pack of standard stickers.
    """

    id: Snowflake
    """
    The ID of the pack.
    """

    stickers: tuple[Sticker, ...]
    """
    The stickers in the pack.
    """

    name: str
    """
    The name of the pack.
    """

    sku_id: Snowflake
    """
    The ID of the pack's SKU.
    """

    description: str
    """
    The description of the pack.
    """

    cover_sticker_id: Snowflake | MISSING = MISSING
    """
    The ID of a sticker in the pack which is shown as the pack's icon.
    """

    banner_asset_id: Snowflake | MISSING = MISSING
    """
    The ID of the pack's banner image.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "stickers": Sticker,
        "sku_id": Snowflake,
        "cover_sticker_id": Snowflake,
        "banner_asset_id": Snowflake,
    }
