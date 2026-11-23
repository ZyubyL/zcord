from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.user.avatar_decoration_data import AvatarDecorationData
from zcord.models.user.collectibles.collectibles import Collectibles
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildMember(Model):
    roles: tuple[Snowflake, ...]
    """Tuple of [`Role`][zcord.Role] IDs."""

    deaf: bool
    """Whether the user is deafened in voice channels."""

    mute: bool
    """Whether the user is muted in voice channels."""

    permissions: str
    """Total permissions of the member in the channel, including overwrites, \
    returned when in the interaction object."""

    user: User | MISSING = MISSING
    """The user this guild member represents."""

    nick: str | None | MISSING = MISSING
    """This user's guild nickname."""

    avatar: str | None | MISSING = MISSING
    """The member's guild avatar hash."""

    bannner: str | None | MISSING = MISSING
    """The member's guild banner hash."""

    joined_at: datetime | None = None
    """When the user joined the guild."""

    premium_since: datetime | None | MISSING = MISSING
    """When the user started boosting the guild."""

    flags: bitfields.GuildMemberFlags = bitfields.GuildMemberFlags.DEFAULT
    """This guild member's flags."""

    pending: bool | MISSING = MISSING
    """Whether the user has not yet passed the guild's membership screening \
    requirement."""

    communication_diabled_until: datetime | None | MISSING = MISSING
    """When the user's timeout will expire and the user will be able to \
    communicate in the guild again, [`None`][] or time in the past if \
    the user is not timed out."""

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """Data for the member's guild avatar decoration."""

    collectibles: Collectibles | None | MISSING = MISSING
    """Data for the member's collectibles."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user": User,
        "roles": Snowflake,
        "joined_at": datetime.fromisoformat,
        "premium_since": datetime.fromisoformat,
        "flags": bitfields.GuildMemberFlags,
        "communication_diabled_until": datetime.fromisoformat,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
    }


type Member = GuildMember
"""An alias to GuildMember."""
