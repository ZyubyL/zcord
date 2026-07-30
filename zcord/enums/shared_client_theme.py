from __future__ import annotations

from enum import IntEnum


class BaseThemeType(IntEnum):
    """
    | Type | Value |
    | ---- | ----- |
    | `UNSET` | `0` |
    | `DARK` | `1` |
    | `LIGHT` | `2` |
    | `DARKER` | `3` |
    | `MIDNIGHT` | `4` |

    Notes:
        `UNSET` is equivalent to `DARK`
    """

    UNSET = 0
    DARK = 1
    LIGHT = 2
    DARKER = 3
    MIDNIGHT = 4
