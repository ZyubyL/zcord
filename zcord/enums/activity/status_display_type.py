from __future__ import annotations

from enum import IntEnum


class StatusDisplayType(IntEnum):
    """Controls which field is displayed in the user's status text \
    in the member list.

    | Name | Value | Example |
    |------|-------|---------|
    | `NAME` | `0` | "Listening to Spotify" |
    | `STATE` | `1` | "Listening to Rick Astley" |
    | `DETAILS` | `2` | "Listening to Never Gonna Give You Up" |
    """

    NAME = 0
    STATE = 1
    DETAILS = 2
