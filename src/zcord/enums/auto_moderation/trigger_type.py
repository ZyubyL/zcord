from enum import IntEnum


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
