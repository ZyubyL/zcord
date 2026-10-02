from __future__ import annotations

from datetime import UTC, datetime

DISCORD_EPOCH = 1420070400000


class Snowflake(int):
    """Discord's unique identifiable descriptor"""

    def __new__(cls, value: int):
        value = int(value)

        if value < 0:
            raise ValueError("Snowflake cannot be negative")

        return super().__new__(cls, value)

    def to_datetime(self) -> datetime:
        """
        Convert this Snowflake to `datetime` object

        Returns:
            The timestamp when this Snowflake is generated
        """
        return datetime.fromtimestamp(
            (self.__rshift__(22) + DISCORD_EPOCH) / 1000, UTC
        )
