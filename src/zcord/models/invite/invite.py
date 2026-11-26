from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import bitfields, enums
from zcord.missing import MISSING
from zcord.models.application.application import Application
from zcord.models.base import Model
from zcord.models.channel.channel import Channel
from zcord.models.guild.guild import Guild
from zcord.models.guild_scheduled_event.scheduled_event import (
    GuildScheduledEvent,
)
from zcord.models.permissons.role.role import Role
from zcord.models.user.user import User


@dataclass(frozen=True, slots=True)
class Invite(Model):
    type: enums.InviteType
    """The type of invite."""

    code: str
    """The invite code (unique ID)."""

    guild: Guild | MISSING = MISSING
    """The guild the invite is for."""

    channel: Channel | None = None
    """The channel this invite is for."""

    inviter: User | MISSING = MISSING
    """The user who created the invite."""

    target_type: enums.InviteTargetType | MISSING = MISSING
    """The type of target for this voice channel invite."""

    target_user: User | MISSING = MISSING
    """The user whose stream to display for this voice channel stream invite."""

    target_application: Application | MISSING = MISSING
    """The embedded application to open \
    for this voice channel embedded application invite."""

    approximate_presence_count: int | MISSING = MISSING
    """Approximate count of online members."""

    approximate_member_count: int | MISSING = MISSING
    """Approximate count of total members."""

    expires_at: datetime | None = None
    """The expiration date of this invite."""

    guild_scheduled_event: GuildScheduledEvent | MISSING = MISSING
    """Guild scheduled event data."""

    flags: bitfields.GuildInviteFlags | MISSING = MISSING
    """Flags for guild invites."""

    roles: tuple[Role, ...] | MISSING = MISSING
    """The roles assigned to the user upon accepting this invite."""

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.InviteType,
        "guild": Guild,
        "channel": Channel,
        "inviter": User,
        "target_type": enums.InviteTargetType,
        "target_user": User,
        "target_application": Application,
        "expires_at": datetime.fromisoformat,
        "guild_scheduled_event": GuildScheduledEvent,
        "flags": bitfields.GuildInviteFlags,
        "roles": Role,
    }
