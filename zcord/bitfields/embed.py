from __future__ import annotations

from enum import IntFlag


class EmbedFlags(IntFlag):
    """
    | Flag | Value |
    |------|-------|
    | `NONE` | `0` |
    | `IS_CONTENT_INVENTORY_ENTRY` | `1 << 5` |
    """

    NONE = 0
    IS_CONTENT_INVENTORY_ENTRY = 1 << 5


class EmbedMediaFlags(IntFlag):
    """
    | Flag | Value |
    |------|-------|
    | `NONE` | `0` |
    | `IS_ANIMATED` | `1 << 5` |
    """

    NONE = 0
    IS_ANIMATED = 1 << 5
