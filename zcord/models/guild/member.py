from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, ClassVar

from zcord import bitfields, cdn, types
from zcord.missing import MISSING
from zcord.models.avatar_decoration_data import AvatarDecorationData
from zcord.models.base import Model
from zcord.models.collectibles import Collectibles
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.guild import Guild


@dataclass(frozen=True, slots=True)
class Member(Model):
    """Represent a Discord guild member."""

    user: User | MISSING = MISSING
    """The user object of this guild member."""

    nick: str | None | MISSING = MISSING
    """The member's guild nickname."""

    avatar: str | None | MISSING = MISSING
    """The member's guild avatar hash.

    Notes:
        This field can be [`None`][] or [`MISSING`][], you can \
        try to use [`Member.user.avatar()`][] instead.
    """

    banner: str | None | MISSING = MISSING
    """The member's guild banner hash.

    Notes:
        This field can be [`None`][] or [`MISSING`][], you can \
        try to use [`Member.user.banner()`][] instead.
    """

    roles: tuple[Snowflake, ...] = ()
    """The member's role IDs."""

    joined_at: datetime | None = None
    """When the member join the guild.

    Notes:
        This is [`None`][] when the member was invited as a guest \
        from the [`GatewayEvent.VOICE_STATE_UPDATE`][] event.
    """

    premium_since: datetime | None | MISSING = MISSING
    """When the member started boosting the guild."""

    deaf: bool = False
    """Whether the member is deafen."""

    mute: bool = False
    """Whether the member is muted."""

    flags: bitfields.MemberFlags = bitfields.MemberFlags.UNKNOWN
    """This member flags."""

    pending: bool | MISSING = MISSING
    """Whether the member has NOT passed the guild's Member Screening."""

    permissions: str | MISSING = MISSING
    """Total permissions of the member in the channel, including overrides, \
    returned when in the [`Interaction`][zcord.Interaction] object."""

    communication_disabled_until: datetime | None | MISSING = MISSING
    """When the member's timeout will expire.

    Notes:
        This is [`None`][] or any time in the past means the user \
        is not timed out.
    """

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """Data for the member's guild avatar decoration."""

    collectibles: Collectibles | None | MISSING = MISSING
    """Data for the member's collectibles."""

    # TODO: Guild injection
    _guild: Guild | None = None

    _transforms: ClassVar[dict] = {
        "user": User,
        "roles": Snowflake,
        "joined_at": datetime.fromisoformat,
        "premium_since": datetime.fromisoformat,
        "flags": bitfields.MemberFlags,
        "communication_disabled_until": datetime.fromisoformat,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
    }

    @property
    def guild(self) -> Guild | None:
        """The member's guild."""
        return self._guild

    @property
    def id(self) -> Snowflake | None:
        """The member's user ID."""
        if self.user is MISSING:
            return None
        return self.user.id

    def avatar_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the member's guild avatar."""
        # Hopefully this will not fail.
        if self.guild is None:
            return None
        if self.avatar is None or self.avatar is MISSING:
            return None
        if self.user is MISSING:
            return None
        return cdn.guild_member_avatar(
            guild_id=self.guild.id,
            user_id=self.user.id,
            hash=self.avatar,
            size=size,
            format=format,
        )

    def banner_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the member's guild banner."""
        # Hopefully this will not fail.
        if self.guild is None:
            return None
        if self.banner is None or self.banner is MISSING:
            return None
        if self.user is MISSING:
            return None
        return cdn.guild_member_banner(
            guild_id=self.guild.id,
            user_id=self.user.id,
            hash=self.banner,
            size=size,
            format=format,
        )

    def avatar_decoration_url(self, size: int = cdn.MAX_SIZE) -> str | None:
        """The URL of the user's avatar decoration."""
        if (
            self.avatar_decoration_data is None
            or self.avatar_decoration_data is MISSING
        ):
            return None
        return self.avatar_decoration_data.asset_url(size=size)
