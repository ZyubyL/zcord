from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild_scheduled_event.scheduled_event_entity_metadata import (
    GuildScheduledEventEntityMetadata,
)
from zcord.models.guild_scheduled_event.scheduled_event_recurrence_rule import (
    GuildScheduledEventRecurrenceRule,
)
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ScheduledEvent(Model):
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


type GuildScheduledEvent = ScheduledEvent
"""An alias to ScheduledEvent."""
