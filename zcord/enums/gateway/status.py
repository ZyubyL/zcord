from __future__ import annotations

from enum import StrEnum


class Status(StrEnum):
    """The status of the [`User`][zcord.User].

    Can also be used to update the bot's status via gateway.

    | Name | Value |
    |------|-------|
    | `ONLINE` | `"online"` |
    | `DND` | `"dnd"` |
    | `IDLE` | `"idle"` |
    | `INVISIBLE` | `"invisible"` |
    | `OFFLINE` | `"offline"` |
    """

    ONLINE = "online"
    DND = "dnd"
    IDLE = "idle"
    INVISIBLE = "invisible"
    OFFLINE = "offline"
