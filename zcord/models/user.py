from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import bitfields
from zcord.cdn import CDN
from zcord.missing import MISSING
from zcord.models.avatar_decoration_data import AvatarDecorationData
from zcord.models.base import Model
from zcord.models.collectibles import Collectibles
from zcord.models.primary_guild import PrimaryGuild
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class User(Model):
    """
    Represent a Discord User
    """

    id: Snowflake
    """
    The user's ID.
    """

    username: str
    """
    The user's username.
    """

    discriminator: str
    """
    The user's Discord tag[^1].

    [^1]: Except bots, this field will be `"0"`.
    """

    global_name: str | None
    """
    The user's display name if it is set.
    """

    avatar: str | None
    """
    The user's avatar hash.
    """

    bot: bool | MISSING = MISSING
    """
    Whether the user is a bot.
    """

    system: bool | MISSING = MISSING
    """
    Whether the user is an **Official Discord System** user.
    """

    mfa_enabled: bool | MISSING = MISSING
    """
    Whether the user has multi factor authentication enabled.
    """

    banner: str | None | MISSING = MISSING
    """
    The user's banner hash.
    """

    accent_color: int | None | MISSING = MISSING
    """
    The user's banner color encoded as an `int`.
    """

    locale: str | MISSING = MISSING
    """
    The user's chosen language option.
    """

    verified: bool | MISSING = MISSING
    """
    Whether the email on this account is verified.
    """

    email: str | None | MISSING = MISSING
    """
    The user's email.
    """

    flags: bitfields.UserFlags | MISSING = MISSING
    """
    The user's account flags.
    """

    premium_type: int | MISSING = MISSING
    """
    The type of Nitro subscription of the user.
    """

    public_flags: bitfields.UserFlags | MISSING = MISSING
    """
    The user's public account flags.
    """

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """
    The user's avatar decoration data.
    """

    collectibles: Collectibles | None | MISSING = MISSING
    """
    The user's collectibles data.
    """

    primary_guild: PrimaryGuild | None | MISSING = MISSING
    """
    The user's primary guild.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "flags": bitfields.UserFlags,
        "public_flags": bitfields.UserFlags,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
        "primary_guild": PrimaryGuild,
    }

    def avatar_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the user's avatar.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.avatar is None:
            return None
        return CDN.user_avatar(
            user_id=self.id,
            hash=self.avatar,
            size=size,
            format=format,
        )

    def banner_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the user's banner.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.banner is None or self.banner is MISSING:
            return None
        return CDN.user_banner(
            user_id=self.id,
            hash=self.banner,
            size=size,
            format=format,
        )

    def avatar_decoration_url(self, size: int = CDN.MAX_SIZE) -> str | None:
        """
        The URL of the user's avatar decoration.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if (
            self.avatar_decoration_data is None
            or self.avatar_decoration_data is MISSING
        ):
            return None
        return self.avatar_decoration_data.asset_url(size=size)
