from __future__ import annotations

from enum import StrEnum


class Status(StrEnum):
    """The status of a [`Presence`][zcord.Presence].

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
