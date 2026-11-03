from __future__ import annotations

from enum import IntEnum


class AgeRestrictionLevel(IntEnum):
    """Guild age-restriction level."""

    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3
