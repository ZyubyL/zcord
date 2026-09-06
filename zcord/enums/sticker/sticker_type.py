from __future__ import annotations

from enum import IntEnum


class StickerType(IntEnum):
    """
    | Type | Value | Description |
    |------|-------|-------------|
    | `STANDARD` | `1` | An official sticker in a pack. |
    | `GUILD` | `2` | A [`Sticker`][zcord.Sticker] uploaded to a guild. |
    """

    STANDARD = 1
    GUILD = 2
