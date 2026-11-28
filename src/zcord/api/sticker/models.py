from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class StickerItem(Model):
    id: Snowflake
    """ID of the sticker."""

    name: str
    """Name of the sticker."""

    format_type: enums.StickerFormatType
    """Type of sticker format."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "format_type": enums.StickerFormatType,
    }


@dataclass(frozen=True, slots=True)
class Sticker(Model):
    id: Snowflake
    """ID of the sticker."""

    name: str
    """Name of the sticker."""

    tags: str
    """Autocomplete/suggestion tags for the sticker."""

    type: enums.StickerType
    """Type of sticker."""

    format_type: enums.StickerFormatType
    """Type of sticker format."""

    description: str | None = None
    """Description of the sticker."""

    pack_id: Snowflake | MISSING = MISSING
    """For standard stickers, id of the pack the sticker is from."""

    available: bool | MISSING = MISSING
    """Whether this guild sticker can be used, \
    may be false due to loss of Server Boosts."""

    guild_id: Snowflake | MISSING = MISSING
    """ID of the guild that owns this sticker."""

    user: User | MISSING = MISSING
    """The user that uploaded the guild sticker."""

    sort_value: int | MISSING = MISSING
    """The standard sticker's sort order within its pack."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.StickerType,
        "format_type": enums.StickerFormatType,
        "pack_id": Snowflake,
        "guild_id": Snowflake,
        "user": User,
    }


@dataclass(frozen=True, slots=True)
class StickerPack(Model):
    id: Snowflake
    """ID of the sticker pack."""

    stickers: tuple[Sticker, ...]
    """The stickers in the pack."""

    name: str
    """Name of the sticker pack."""

    sku_id: Snowflake
    """ID of the pack's SKU."""

    description: str
    """Description of the sticker pack."""

    cover_sticker_id: Snowflake | MISSING = MISSING
    """ID of a sticker in the pack which is shown as the pack's icon."""

    banner_asset_id: Snowflake | MISSING = MISSING
    """ID of the sticker pack's banner image."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "stickers": Sticker,
        "sku_id": Snowflake,
        "cover_sticker_id": Snowflake,
        "banner_asset_id": Snowflake,
    }
