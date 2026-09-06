from __future__ import annotations

from enum import IntEnum


class MessageActivityType(IntEnum):
    """
    Type of message activity.

    | Type | Value |
    |------|-------|
    | `JOIN` | `1` |
    | `SPECTATE` | `2` |
    | `LISTEN` | `3` |
    | `JOIN_REQUEST` | `5` |
    """

    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5
