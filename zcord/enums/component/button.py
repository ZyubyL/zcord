from __future__ import annotations

from enum import IntEnum


class ButtonStyle(IntEnum):
    """
    | Name | Value |
    |------|-------|
    | `PRIMARY` | `1` |
    | `SECONDARY` | `2` |
    | `SUCCESS` | `3` |
    | `DANGER` | `4` |
    | `LINK` | `5` |
    | `PREMIUM` | `6` |
    """

    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5
    PREMIUM = 6
