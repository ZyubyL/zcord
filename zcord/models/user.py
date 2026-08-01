from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.cdn import CDN
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class User(ZcordModel):
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
    flags: int | MISSING = MISSING
    premium_type: int | MISSING = MISSING
    public_flags: int | MISSING = MISSING
    avatar_decoration_data: Any | None | MISSING = MISSING
    collectibles: Any | None | MISSING = MISSING
    primary_guild: Any | None | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }

    @property
    def avatar_url(self) -> str | None:
        if self.avatar is None:
            return None
        return CDN.user_avatar(self.id, self.avatar)

    @property
    def banner_url(self) -> str | None:
        if self.banner is None or self.banner is MISSING:
            return None
        return CDN.user_banner(self.id, self.banner)
