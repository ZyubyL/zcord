from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.models.channel.channel import Channel
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildWidget(Model):
    id: Snowflake
    """Guild ID."""

    name: str
    """Guild name."""

    instant_invite: str | None
    """Instant invite for the guilds specified widget invite channel."""

    channels: tuple[Channel, ...]
    """Voice and stage channels which are accessible by @everyone."""

    members: tuple[User, ...]
    """Special widget user objects that includes users presence."""

    presence_count: int
    """Number of online member in this guild."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "channels": Channel,
        "members": User,
    }
