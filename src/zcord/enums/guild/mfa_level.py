from enum import IntEnum


class MFALevel(IntEnum):
    NONE = 0
    """Guild has no MFA/2FA requirement for moderation actions."""

    ELEVATED = 1
    """Guild has 2FA requirement for moderation actions."""
