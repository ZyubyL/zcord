from enum import IntEnum


class EventType(IntEnum):
    MESSAGE_SEND = 1
    """When a member sends or edits a message in the guild."""

    MEMBER_UPDATE = 2
    """When a member edits their profile."""
