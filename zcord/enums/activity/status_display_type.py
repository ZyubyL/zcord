from __future__ import annotations

from enum import IntEnum


class StatusDisplayType(IntEnum):
    """Controls which field is displayed in the user's status text \
    in the member list.

    | Name (library named) | Value | Example |
    |----------------------|-------|---------|
    | `PLATFORM` | `0` | "Listening to Spotify" |
    | `ARTIST` | `1` | "Listening to Rick Astley" |
    | `SONG` | `2` | "Listening to Never Gonna Give You Up" |
    """

    PLATFORM = 0
    ARTIST = 1
    SONG = 2
