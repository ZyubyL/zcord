from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.cdn import CDN
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class PrimaryGuild(Model):
    """
    Represent the user's primary guild.

    Attributes:
        identity_guild_id:
            The ID of the user's primary guild.
        identity_enabled:
            Whether the user displaying the primary guild's server tag.
            This will be `None` if the system clears the identity,
            and `False` if the user manually removed their tag.
        tag:
            The text of the user's tag. Max `4` characters.
        badge:
            The server tag badge.
    """

    identity_guild_id: Snowflake | None
    identity_enabled: bool | None
    tag: str | None
    badge: str | None

    _transforms: ClassVar[dict] = {
        "identity_guild_id": Snowflake,
    }

    def badge_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp"] | None = None,
    ) -> str | None:
        """
        The URL of the user's primary guild's badge.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.identity_guild_id is None or self.badge is None:
            return None
        return CDN.badge(
            guild_id=self.identity_guild_id,
            hash=self.badge,
            size=size,
            format=format,
        )
