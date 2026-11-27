from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.api.guild.models import GuildMember
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildScheduledEventEntityMetadata(Model):
    location: str | MISSING = MISSING
    """Location of the event."""


@dataclass(frozen=True, slots=True)
class GuildScheduledEventRecurrenceRuleNWeekday(Model):
    n: int
    """The week to reoccur on (1-5)."""

    day: enums.ScheduledEventRecurrenceRuleWeekday
    """The day within the week to reoccur on."""

    _transforms: ClassVar[dict[str, Any]] = {
        "day": enums.ScheduledEventRecurrenceRuleWeekday
    }


@dataclass(frozen=True, slots=True)
class GuildScheduledEventUser(Model):
    guild_scheduled_event_id: Snowflake
    """The scheduled event ID which the user subscribed to."""

    user: User
    """User which subscribed to an event."""

    member: GuildMember | MISSING = MISSING
    """Guild member data for this user for the guild \
    which this event belongs to, if any."""

    _transforms: ClassVar[dict[str, Any]] = {
        "guild_scheduled_event_id": Snowflake,
        "user": User,
        "member": GuildMember,
    }


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


@dataclass(frozen=True, slots=True)
class GuildScheduledEvent(Model):
    id: Snowflake
    """The ID of the scheduled event."""

    guild_id: Snowflake
    """The guild ID which the scheduled event belongs to."""

    name: str
    """The name of the scheduled event."""

    scheduled_start_time: datetime
    """The time the scheduled event will start."""

    privacy_level: enums.PrivacyLevel
    """The privacy level of the scheduled event."""

    status: enums.ScheduledEventStatus
    """The status of the scheduled event."""

    entity_type: enums.ScheduledEntityType
    """The type of the scheduled event."""

    entity_metadata: GuildScheduledEventEntityMetadata
    """Additional metadata for the guild scheduled event."""

    user_count: int
    """The number of users subscribed to the scheduled event."""

    channel_id: Snowflake | None = None
    """The channel ID in which the scheduled event will be hosted, \
    or [`None`][] if `entity_type` is `EXTERNAL`."""

    creator_id: Snowflake | None | MISSING = MISSING
    """The ID of the user that created the scheduled event.

    Notes:
        `creator_id` will be [`None`][] and `creator` will not be included \
        for events created before October 25th, 2021, \
        when the concept of `creator_id` was introduced and tracked.
    """

    description: str | None | MISSING = MISSING
    """The description of the scheduled event."""

    scheduled_end_time: datetime | None = None
    """The time the scheduled event will end, \
    required if `entity_type` is `EXTERNAL`."""

    entity_id: Snowflake | None = None
    """The ID of an entity associated with a guild scheduled event."""

    creator: User | MISSING = MISSING
    """The user that created the scheduled event.

    Notes:
        `creator_id` will be [`None`][] and `creator` will not be included \
        for events created before October 25th, 2021, \
        when the concept of `creator_id` was introduced and tracked.
    """

    image: str | None | MISSING = MISSING
    """The cover image hash of the scheduled event."""

    recurrence_rule: GuildScheduledEventRecurrenceRule | None = None
    """The definition for how often this event should recur."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "guild_id": Snowflake,
        "channel_id": Snowflake,
        "creator_id": Snowflake,
        "scheduled_start_time": datetime.fromisoformat,
        "scheduled_end_time": datetime.fromisoformat,
        "privacy_level": enums.PrivacyLevel,
        "status": enums.ScheduledEventStatus,
        "entity_type": enums.ScheduledEntityType,
        "entity_id": Snowflake,
        "entity_metadata": GuildScheduledEventEntityMetadata,
        "creator": User,
        "recurrence_rule": GuildScheduledEventRecurrenceRule,
    }
