from enum import IntEnum


class ApplicationRoleConnectionMetadataTypes(IntEnum):
    INTEGER_LESS_THAN_OR_EQUAL = 1
    """The metadata value (int) is less than or equal to the guild's \
    configured value (int)."""

    INTEGER_GREATER_THAN_OR_EQUAL = 2
    """The metadata value (int) is greater than or equal to the guild's \
    configured value (int)."""

    INTEGER_EQUAL = 3
    """The metadata value (int) is equal to the guild's \
    configured value (int)."""

    INTEGER_NOT_EQUAL = 4
    """The metadata value (int) is not equal to the guild's \
    configured value (int)."""

    DATETIME_LESS_THAN_OR_EQUAL = 5
    """The metadata value (datetime) is less than or equal to the guild's \
    configured value (int; days before current date)."""

    DATETIME_GREATER_THAN_OR_EQUAL = 6
    """The metadata value (datetime) is greater than or equal to the guild's \
    configured value (int; days before current date)."""

    BOOLEAN_EQUAL = 7
    """The metadata value (int) is equal to the guild's \
    configured value (int; 1)."""

    BOOLEAN_NOT_EQUAL = 8
    """The metadata value (int) is not equal to the guild's \
    configured value (int; 1)."""
