from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivityTimestamp(Model):
    """Contain the activity timestamp info."""

    start: int | MISSING = MISSING
    """Unix time (in milliseconds) of when the activity started.

    Notes:
        This is what Discord send. Use `start_time` if you want a \
        [`datetime`][datetime.datetime] object.
    """

    end: int | MISSING = MISSING
    """Unix time (in milliseconds) of when the activity ends.

    Notes:
        This is what Discord send. Use `end_time` if you want a \
        [`datetime`][datetime.datetime] object.
    """

    @staticmethod
    def _to_datetime(v: int | MISSING) -> datetime | MISSING:
        if v is MISSING:
            return MISSING
        return datetime.fromtimestamp(v / 1000, UTC)

    @property
    def start_time(self) -> datetime | MISSING:
        """The datetime when the activity started."""
        return self._to_datetime(self.start)

    @property
    def end_time(self) -> datetime | MISSING:
        """The datetime when the activity ends."""
        return self._to_datetime(self.end)
