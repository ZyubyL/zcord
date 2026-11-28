from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class StageInstance(Model):
    id: Snowflake
    """The ID of this Stage instance."""

    guild_id: Snowflake
    """The guild ID of the associated Stage channel."""

    channel_id: Snowflake
    """The ID of the associated Stage channel."""

    topic: str
    """The topic of the Stage instance."""

    privacy_level: enums.PrivacyLevel
    """The privacy level of the Stage instance."""

    guild_scheduled_event_id: Snowflake | None = None
    """The ID of the scheduled event for this Stage instance."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "guild_id": Snowflake,
        "channel_id": Snowflake,
        "privacy_level": enums.PrivacyLevel,
        "guild_scheduled_event_id": Snowflake,
    }
