from __future__ import annotations

from enum import IntEnum


class StickerFormatType(IntEnum):
    """
    | Type | Value |
    |------|-------|
    | `PNG` | `1` |
    | `APNG` | `2` |
    | `LOTTIE` | `3` |
    | `GIF` | `4` |
    """

    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4
