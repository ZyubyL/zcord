from __future__ import annotations

from enum import IntFlag


class RoleFlags(IntFlag):
    """
    | Flag | Value |
    |------|-------|
    | `NONE` | `0` |
    | `IN_PROMPT` | `1 << 0` |
    """

    NONE = 0
    IN_PROMPT = 1 << 0
