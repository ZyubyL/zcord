from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class GuildScheduledEventRecurrenceRuleNWeekday(Model):
    n: int
    """The week to reoccur on (1-5)."""

    day: enums.ScheduledEventRecurrenceRuleWeekday
    """The day within the week to reoccur on."""

    _transforms: ClassVar[dict[str, Any]] = {
        "day": enums.ScheduledEventRecurrenceRuleWeekday
    }
