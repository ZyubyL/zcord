from enum import StrEnum


class TimestampStyle(StrEnum):
    """Unix timestamp format type.

    See this for more info: https://docs.discord.com/developers/reference#message-formatting
    """

    SHORT_TIME = "t"
    MEDIUM_TIME = "T"
    SHORT_DATE = "d"
    LONG_DATE = "D"
    LONG_DATE_SHORT_TIME = "f"
    FULL_DATE_SHORT_TIME = "F"
    SHORT_DATE_SHORT_TIME = "s"
    SHORT_DATE_MEDIUM_TIME = "S"
    RELATIVE_TIME = "R"

    DEFAULT = LONG_DATE_SHORT_TIME
