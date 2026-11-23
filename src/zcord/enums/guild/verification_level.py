from enum import IntEnum


class VerificationLevel(IntEnum):
    NONE = 0
    """Unrestricted."""

    LOW = 1
    """Must have verified email on account."""

    MEDIUM = 2
    """Must be registered on Discord for longer than 5 minutes."""

    HIGH = 3
    """Must be a member of the server for longer than 10 minutes."""

    VERY_HIGH = 4
    """Must have a verified phone number."""
