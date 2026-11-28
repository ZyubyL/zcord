from enum import IntEnum


class StickerType(IntEnum):
    STANDARD = 1
    """An official sticker in a pack."""

    GUILD = 2
    """A sticker uploaded to a guild for the guild's members."""


class StickerFormatType(IntEnum):
    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4
