from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields, cdn, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.user.avatar_decoration_data import AvatarDecorationData
from zcord.models.user.collectibles.collectibles import Collectibles
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class User(Model):
    """Represent a Discord user."""

    id: Snowflake
    """The user's ID."""

    username: str
    """The user's username."""

    discriminator: str
    """The user's Discord tag[^1].

    [^1]: Except bots, this field will be `"0"`.
    """

    global_name: str | None
    """The user's display name if it is set."""

    avatar: str | None
    """The user's avatar hash."""

    bot: bool | MISSING = MISSING
    """Whether the user is a bot."""

    system: bool | MISSING = MISSING
    """Whether the user is an **Official Discord System** user."""

    mfa_enabled: bool | MISSING = MISSING
    """Whether the user has two factor authentication enabled on \
    their account."""

    banner: str | None | MISSING = MISSING
    """The user's banner hash."""

    accent_color: int | None | MISSING = MISSING
    """The user's banner color encoded as an `int`."""

    locale: str | MISSING = MISSING
    """The user's chosen language option."""

    verified: bool | MISSING = MISSING
    """Whether the email on this account is verified."""

    email: str | None | MISSING = MISSING
    """The user's email."""

    flags: bitfields.UserFlags | MISSING = MISSING
    """The user account's flags."""

    premium_type: int | MISSING = MISSING
    """The type of Nitro subsciption on this user account."""

    public_flags: bitfields.UserFlags | MISSING = MISSING
    """The user account's public flags."""

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """The user's avatar decoration data."""

    collectibles: Collectibles | None | MISSING = MISSING
    """The user's collectibles data."""

    primary_guild: PrimaryGuild | None | MISSING = MISSING
    """The user's primary guild."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "flags": bitfields.UserFlags,
        "public_flags": bitfields.UserFlags,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
        "primary_guild": PrimaryGuild,
    }

    def avatar_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the user's avatar."""
        if self.avatar is None:
            return None
        return cdn.user_avatar(
            user_id=self.id,
            hash=self.avatar,
            size=size,
            format=format,
        )

    def banner_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the user's banner."""
        if self.banner is None or self.banner is MISSING:
            return None
        return cdn.user_banner(
            user_id=self.id,
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
