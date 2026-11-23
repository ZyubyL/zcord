from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import cdn, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildPreview(Model):
    id: Snowflake
    """Guild ID."""

    name: str
    """Guild name."""

    icon: str | None
    """Icon hash."""

    splash: str | None
    """Splash hash."""

    discovery_splash: str | None
    """Discovery splash hash."""

    emojis: tuple[Emoji, ...]
    """Custom guild emoji."""

    features: tuple[str, ...]
    """Enabled guild features."""

    approximate_member_count: int
    """Approximate number of members in this guild."""

    approximate_presence_count: int
    """Approximate number of online members in this guild."""

    description: str | None
    """The description of the guild."""

    stickers: tuple[Sticker, ...]
    """Custom guild stickers."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "emojis": Emoji,
        "stickers": Sticker,
    }

    def icon_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the guild's icon."""
        if self.icon is None or self.icon is MISSING:
            return None
        return cdn.guild_icon(
            guild_id=self.id,
            hash=self.icon,
            size=size,
            format=format,
        )

    def splash_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The URL of the guild's splash."""
        if self.splash is None:
            return None
        return cdn.guild_splash(
            guild_id=self.id,
            hash=self.splash,
            size=size,
            format=format,
        )

    def discovery_splash_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The URL of the guild's discovery splash.

        Notes:
            Only present if guild has `DISCOVERABLE` feature.
        """
        if self.splash is None:
            return None
        return cdn.guild_discovery_splash(
            guild_id=self.id,
            hash=self.splash,
            size=size,
            format=format,
        )
