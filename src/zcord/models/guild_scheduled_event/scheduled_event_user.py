from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild.guild_member import GuildMember
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ScheduledEventUser(Model):
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


type GuildScheduledEventUser = ScheduledEventUser
"""An alias to ScheduledEventUser."""
