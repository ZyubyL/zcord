from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from zcord.cdn import CDN
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake

if TYPE_CHECKING:
    from zcord import types


@dataclass(frozen=True, slots=True)
class PrimaryGuild(Model):
    """
    Represent the user's primary guild.
    """

    identity_guild_id: Snowflake | None
    """
    The ID of the user's primary guild.
    """

    identity_enabled: bool | None
    """
    Whether the user displaying the primary guild's server tag.
    This will be `None` if the system clears the identity,
    and `False` if the user manually removed their tag.
    """

    tag: str | None
    """
    The text of the user's tag. Max `4` characters.
    """

    badge: str | None
    """
    The server tag badge.
    """

    _transforms: ClassVar[dict] = {
        "identity_guild_id": Snowflake,
    }

    def badge_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """
        The URL of the user's primary guild's badge.
        """
        if self.identity_guild_id is None or self.badge is None:
            return None
        return CDN.badge(
            guild_id=self.identity_guild_id,
            hash=self.badge,
            size=size,
            format=format,
        )
