from __future__ import annotations

from enum import IntEnum


class ExplicitContentFilterLevel(IntEnum):
    """
    The explicit content filtering level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `DISABLED` | `0` | Media content will not be scanned. |
    | `MEMBERS_WITHOUT_ROLES` | `1` | Media content sent by members without \
    roles will be scanned. |
    | `ALL_MEMBERS` | `2` | Media content sent by all members will be scanned. |
    """

    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2
