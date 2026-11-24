from enum import IntEnum


class ActionType(IntEnum):
    BLOCK_MESSAGE = 1
    """Blocks a member's message and prevents it from being posted.
    A custom explanation can be specified and shown to members \
    whenever their message is blocked."""

    SEND_ALERT_MESSAGE = 2
    """Logs user content to a specified channel."""

    TIMEOUT = 3
    """Timeout user for a specified duration.

    Notes:
        Can only be set up for `KEYWORD` and `MENTION_SPAM` rules. \
        The `MODERATE_MEMBERS` permission is required to use this action type.
    """

    BLOCK_MEMBER_INTERACTION = 4
    """Prevents a member from using text, voice, or other interactions."""
