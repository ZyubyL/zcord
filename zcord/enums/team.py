from __future__ import annotations

from enum import IntEnum


class MembershipState(IntEnum):
    """
    | Type | Value |
    |------|-------|
    | `INVITED` | `0` |
    | `ACCEPTED` | `1` |
    """

    INVITED = 0
    ACCEPTED = 1
