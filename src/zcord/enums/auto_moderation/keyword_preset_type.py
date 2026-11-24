from enum import IntEnum


class KeywordPresetType(IntEnum):
    PROFANITY = 1
    """Words that may be considered forms of swearing or cursing."""

    SEXUAL_CONTENT = 2
    """Words that refer to sexually explicit behavior or activity."""

    SLURS = 3
    """Personal insults or words that may be considered hate speech."""
