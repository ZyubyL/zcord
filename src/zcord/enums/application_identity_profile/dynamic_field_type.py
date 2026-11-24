from enum import IntEnum


class DynamicFieldType(IntEnum):
    STRING = 0
    """A text value."""

    NUMBER = 1
    """A numeric value."""

    MEDIA = 2
    """A [`Media`][zcord.Media] object."""
