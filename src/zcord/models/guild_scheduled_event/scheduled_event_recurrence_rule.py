from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model
from zcord.models.guild_scheduled_event.scheduled_event_recurrence_rule_n_weekday import (  # noqa: E501
    GuildScheduledEventRecurrenceRuleNWeekday,
)


@dataclass(frozen=True, slots=True)
class GuildScheduledEventRecurrenceRule(Model):
    frequency: enums.ScheduledEventRecurrenceRuleFrequency
    """How often the event occurs."""

    interval: int
    """The spacing between the events, defined by `frequency`.

    For example, `frequency` of `WEEKLY` and an interval of `2` \
    would be "every other week"."""

    start: datetime
    """Starting time of the recurrence interval."""

    end: datetime | None = None
    """Ending time of the recurrence interval.

    Notes:
        Cannot be set externally currently.
    """

    by_weekday: tuple[enums.ScheduledEventRecurrenceRuleWeekday, ...] | None = (
        None
    )
    """Tuple of specific days within a week for the event to recur on."""

    by_n_weekday: (
        tuple[GuildScheduledEventRecurrenceRuleNWeekday, ...] | None
    ) = None
    """Tuple of specific days within a specific week (1-5) to recur on."""

    by_month: tuple[enums.ScheduledEventRecurrenceRuleMonth, ...] | None = None
    """Tuple of specific month to recur on."""

    by_month_day: tuple[int, ...] | None = None
    """Tuple of specific dates within a month to recur on."""

    by_year_day: tuple[int, ...] | None = None
    """Tuple of days within a year to recur on (1-364).

    Notes:
        Cannot be set externally currently.
    """

    count: int | None = None
    """The total amount of times that the event is allowed \
    to recur before stopping."""

    _transforms: ClassVar[dict[str, Any]] = {
        "frequency": enums.ScheduledEventRecurrenceRuleFrequency,
        "start": datetime.fromisoformat,
        "end": datetime.fromisoformat,
        "by_weekday": enums.ScheduledEventRecurrenceRuleWeekday,
        "by_n_weekday": GuildScheduledEventRecurrenceRuleNWeekday,
        "by_month": enums.ScheduledEventRecurrenceRuleMonth,
    }
