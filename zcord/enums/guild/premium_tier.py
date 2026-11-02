from __future__ import annotations

from enum import IntEnum


class PremiumTier(IntEnum):
    """Server boost tier"""

    NONE = 0
    """Guild has not unlocked any Server Boost perks."""

    TIER_1 = 1
    """Guild has unlocked Server Boost level 1 perks."""

    TIER_2 = 2
    """Guild has unlocked Server Boost level 2 perks."""

    TIER_3 = 3
    """Guild has unlocked Server Boost level 3 perks."""
