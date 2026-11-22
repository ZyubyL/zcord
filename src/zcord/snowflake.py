from __future__ import annotations

from datetime import UTC, datetime
from typing import Final

DISCORD_EPOCH: Final[int] = 1_420_070_400_000


class Snowflake(int):
    """Discord's Unique identifiable descriptor."""

    def __new__(cls, value: int):
        value = int(value)

        if value < 0:
            raise ValueError("Snowflake cannot be nagative")

        return super().__new__(cls, value)

    def to_datetime(self) -> datetime:
        """Convert this Snowflake to a `datetime` object.

        Returns:
            The timestamp when this Snowflake is generated.
        """
        return datetime.fromtimestamp(
            (self.__rshift__(22) + DISCORD_EPOCH) / 1000, UTC
        )
