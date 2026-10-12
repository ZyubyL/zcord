from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivityTimestamp(Model):
    start: int | MISSING = MISSING
    end: int | MISSING = MISSING

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
