from __future__ import annotations

from enum import IntEnum


class MFALevel(IntEnum):
    """
    The MFA level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `NONE` | `0` | No MFA requirement for moderation actions. |
    | `ELEVATED` | `1` | The guild has MFA requirement for moderation actions. |
    """

    NONE = 0
    ELEVATED = 1
