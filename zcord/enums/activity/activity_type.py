from __future__ import annotations

from enum import IntEnum


class ActivityType(IntEnum):
    """The type of an [`Activity`][zcord.Activity].

    | Name | Value |
    |------|-------|
    | `PLAYING` | `0` |
    | `STREAMING` | `1` |
    | `LISTENING` | `2` |
    | `WATCHING` | `3` |
    | `CUSTOM` | `4` |
    | `COMPETING` | `5` |
    """

    PLAYING = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5
