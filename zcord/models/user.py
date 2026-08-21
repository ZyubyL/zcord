from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.cdn import CDN
from zcord.flags.user import UserFlags
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

    Attributes:
        id:
            The user's ID.
        username:
            The user's username.
        discriminator:
            The user's Discord tag.

            **Notes**: Except bots, this field will be `0`.
        global_name:
            The user's display name if it is set.
        avatar:
            The user's avatar hash.
        bot:
            Whether the user is a bot.
        system:
            Whether the user is an **Official Discord System** user.
        mfa_enabled:
            Whether the user has multi factor authentication enabled.
        banner:
            The user's banner hash.
        accent_color:
            The user's banner color encoded as an `int`.
        locale:
            The user's chosen language option.
        verified:
            Whether the email on this account is verified.
        email:
            The user's email.
        flags:
            The user's account flags.
        premium_type:
            The type of Nitro subscription of the user.
        public_flags:
            The user's public account flags.
        avatar_decoration_data:
            The user's avatar decoration data.
        collectibles:
            The user's collectibles data.
        primary_guild:
            The user's primary guild.
    """

    id: Snowflake
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: bool | MISSING = MISSING
    system: bool | MISSING = MISSING
    mfa_enabled: bool | MISSING = MISSING
    banner: str | None | MISSING = MISSING
    accent_color: int | None | MISSING = MISSING
    locale: str | MISSING = MISSING
    verified: bool | MISSING = MISSING
    email: str | None | MISSING = MISSING
    flags: UserFlags | MISSING = MISSING
    premium_type: int | MISSING = MISSING
    public_flags: UserFlags | MISSING = MISSING
    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    collectibles: Collectibles | None | MISSING = MISSING
    primary_guild: PrimaryGuild | None | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "flags": UserFlags,
        "public_flags": UserFlags,
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
