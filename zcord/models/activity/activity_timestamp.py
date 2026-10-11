from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivityTimestamp(Model):
    start: datetime | MISSING = MISSING
    end: datetime | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "start": datetime.fromisoformat,
        "end": datetime.fromisoformat,
    }
