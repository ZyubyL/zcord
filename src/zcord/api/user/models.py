from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Literal

from zcord import bitfields, cdn, enums, errors, types
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class UserPrimaryGuild(Model):
    identity_guild_id: Snowflake | None = None
    """The ID of the user's primary guild."""

    identity_enabled: bool | None = None
    """Whether the user is displaying the primary guild's server tag. \
    This can be [`None`][] if the system clears the identity, \
    e.g. the server no longer supports tags. \
    This will be [`False`][] if the user manually removes their tag."""

    tag: str | None = None
    """The text of the user's server tag. Limited to 4 characters."""

    badge: str | None = None
    """The server tag badge hash."""

    _transforms: ClassVar[dict[str, Any]] = {
        "identity_guild_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class Nameplate(Model):
    """Contain info about the user's nameplate."""

    sku_id: Snowflake
    """The ID of the nameplate SKU."""

    asset: str
    """Path to the nameplate asset."""

    label: str
    """The label of the nameplate[^1].

    [^1]: This field is unused.
    """

    palette: Literal[
        "crimson",
        "berry",
        "sky",
        "teal",
        "forest",
        "bubble_gum",
        "violet",
        "cobalt",
        "clover",
        "lemon",
        "white",
    ]
    """The background color of the nameplate."""

    _transforms: ClassVar[dict[str, Any]] = {
        "sku_id": Snowflake,
    }

    def url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str:
        raise errors.ZcordError(
            """Discord doesn't provide nameplate URL.
            So this will raise an error until they update their docs."""
        )


@dataclass(frozen=True, slots=True)
class Collectibles(Model):
    """Contain info about the user's collectibles."""

    nameplate: Nameplate | MISSING = MISSING
    """The user's nameplate."""

    _transforms: ClassVar[dict[str, Any]] = {
        "nameplate": Nameplate,
    }

    def nameplate_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The URL of the user's nameplate."""
        if self.nameplate is MISSING:
            return None

        return self.nameplate.url(size=size, format=format)


@dataclass(frozen=True, slots=True)
class AvatarDecorationData(Model):
    """Contain data about the user's avatar decoration."""

    asset: str
    """The avatar decoration hash."""

    sku_id: Snowflake
    """The SKU ID of the avatar decoration."""

    _transforms: ClassVar[dict[str, Any]] = {
        "sku_id": Snowflake,
    }

    def asset_url(self, size: int = cdn.MAX_SIZE) -> str:
        """The URL of the avatar decoration asset."""
        return cdn.avatar_decoration(hash=self.asset, size=size)


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

    global_name: str | None = None
    """The user's display name if it is set."""

    avatar: str | None = None
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

    premium_type: enums.PremiumType | MISSING = MISSING
    """The type of Nitro subsciption on this user account."""

    public_flags: bitfields.UserFlags | MISSING = MISSING
    """The user account's public flags."""

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """The user's avatar decoration data."""

    collectibles: Collectibles | None | MISSING = MISSING
    """The user's collectibles data."""

    primary_guild: UserPrimaryGuild | None | MISSING = MISSING
    """The user's primary guild."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "flags": bitfields.UserFlags,
        "premium_type": enums.PremiumType,
        "public_flags": bitfields.UserFlags,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
        "primary_guild": UserPrimaryGuild,
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
