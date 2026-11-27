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


class EventType(IntEnum):
    MESSAGE_SEND = 1
    """When a member sends or edits a message in the guild."""

    MEMBER_UPDATE = 2
    """When a member edits their profile."""


class KeywordPresetType(IntEnum):
    PROFANITY = 1
    """Words that may be considered forms of swearing or cursing."""

    SEXUAL_CONTENT = 2
    """Words that refer to sexually explicit behavior or activity."""

    SLURS = 3
    """Personal insults or words that may be considered hate speech."""


class TriggerType(IntEnum):
    KEYWORD = 1
    """Check if content contains words from a user defined list of keywords.

    Max per guild: 6."""
    SPAM = 3
    """Check if content represents generic spam.

    Max per guild: 1."""
    KEYWORD_PRESET = 4
    """Check if content contains words from internal pre-defined wordsets.

    Max per guild: 1."""
    MENTION_SPAM = 5
    """Check if content contains more unique mentions than allowed.

    Max per guild: 1."""
    MEMBER_PROFILE = 6
    """Check if member profile contains words from a user defined list \
    of keywords.

    Max per guild: 1."""
