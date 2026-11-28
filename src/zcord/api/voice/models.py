from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.api.guild.models import GuildMember
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class VoiceRegion(Model):
    id: str
    """Unique ID for the region."""

    name: str
    """Name of the region."""

    optimal: bool
    """[`True`][] for a single server that is closest \
    to the current user's client."""

    deprecated: bool
    """Whether this is a deprecated voice region (avoid switching to these)."""

    custom: bool
    """Whether this is a custom voice region (used for events/etc)."""


@dataclass(frozen=True, slots=True)
class VoiceState(Model):
    user_id: Snowflake
    """The user ID this voice state is for."""

    session_id: str
    """The session ID for this voice state."""

    deaf: bool
    """Whether this user is deafened by the server."""

    mute: bool
    """Whether this user is muted by the server."""

    self_deaf: bool
    """Whether this user is locally deafened."""

    self_mute: bool
    """Whether this user is locally muted."""

    self_video: bool
    """Whether this user's camera is enabled."""

    suppress: bool
    """Whether this user's permission to speak is denied."""

    guild_id: Snowflake | MISSING = MISSING
    """The guild ID this voice state is for."""

    channel_id: Snowflake | None = None
    """The channel ID this user is connected to."""

    member: GuildMember | MISSING = MISSING
    """The guild member this voice state is for."""

    self_stream: bool | MISSING = MISSING
    """Whether this user is streaming using "Go Live"."""

    request_to_speak_timestamp: datetime | None = None
    """The time at which the user requested to speak."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user_id": Snowflake,
        "guild_id": Snowflake,
        "channel_id": Snowflake,
        "member": GuildMember,
        "request_to_speak_timestamp": datetime.fromisoformat,
    }
