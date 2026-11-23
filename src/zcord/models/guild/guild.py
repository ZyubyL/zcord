from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields, cdn, enums, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild.incidents_data import IncidentsData
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Guild(Model):
    """Represent a Discord server."""

    id: Snowflake
    """The ID of the guild."""

    name: str
    """The name of the guild."""

    icon: str | None
    """The icon hash of the guild."""

    splash: str | None
    """The splash hash of the guild."""

    discovery_splash: str | None
    """The discovery splash hash of the guild with "DISCOVERABLE" feature."""

    owner_id: Snowflake
    """The ID of the owner."""

    afk_channel_id: Snowflake | None
    """The ID of the AFK channel."""

    afk_timeout: int
    """AFK timeout, in seconds."""

    verification_level: enums.VerificationLevel
    """Verification level of the guild."""

    default_message_notifications: enums.DefaultMessageNotificationLevel
    """Default message notification level."""

    explicit_content_filter: enums.ExplicitContentFilterLevel
    """Explicit content filter level."""

    roles: tuple[Role, ...]
    """A tuple of roles in the guild."""

    emojis: tuple[Emoji, ...]
    """A tuple of custom guild emoji."""

    features: tuple[str, ...]
    """A list of enabled guild features."""

    mfa_level: enums.MFALevel
    """Required MFA level for the guild."""

    application_id: Snowflake | None
    """Application ID of the guild creator if it's bot-created."""

    system_channel_id: Snowflake | None
    """The ID of the channel where system messages are sent."""

    system_channel_flags: bitfields.SystemChannelFlags
    """System channel flags."""

    rules_channel_id: Snowflake | None
    """The ID of the rules and/or guidelines channel."""

    vanity_url_code: str | None
    """The vanity URL code for the guild."""

    description: str | None
    """The guild's description."""

    banner: str | None
    """The guild's banner hash."""

    premium_tier: enums.PremiumTier
    """Guild boost level."""

    preferred_locale: str
    """The preferred locale of the Community guild."""

    public_updates_channel_id: Snowflake | None
    """The ID of the channel where admins and moderators of Community \
    guilds receive notices from Discord."""

    nsfw_level: enums.AgeRestrictionLevel
    """Guild age-restriction level."""

    premium_progress_bar_enabled: bool
    """Whether the guild has the boost progress bar enabled."""

    safety_alerts_channel_id: Snowflake | None
    """The ID fo the channel where admins and moderators of Community \
    guilds receive safety alerts from Discord."""

    incidents_data: IncidentsData | None
    """The incidents data of this guild."""

    icon_hash: str | None | MISSING = MISSING
    """The icon hash of the guild when in a guild template."""

    owner: bool | MISSING = MISSING
    """If the user is the owner of the guild."""

    widget_enabled: bool | MISSING = MISSING
    """Whether the guild widget is enabled."""

    widget_channel_id: Snowflake | None | MISSING = MISSING
    """The channel ID that the widget will generate an invite to."""

    max_presences: int | None | MISSING = MISSING
    """The maximum number of presences for the guild."""

    max_members: int | None | MISSING = MISSING
    """The maximum number of members for the guild."""

    premium_subscription_count: int | MISSING = MISSING
    """The number of boosts this guild currently has."""

    max_video_channel_users: int | MISSING = MISSING
    """The maximum amount of users in a video channel."""

    max_stage_video_channel_users: int | MISSING = MISSING
    """The maximum amount of users in a stage video channel."""

    approximate_member_count: int | MISSING = MISSING
    """Approximate number of members in this guild."""

    approximate_presence_count: int | MISSING = MISSING
    """Approximate number of non-offline members in this guild."""

    welcome_screen: Any | MISSING = MISSING
    """The welcome screen of a Community guild shown to new members."""

    stickers: tuple[Sticker, ...] | MISSING = MISSING
    """A tuple of custom guild stickers."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "owner_id": Snowflake,
        "afk_channel_id": Snowflake,
        "verification_level": enums.VerificationLevel,
        "default_message_notifications": enums.DefaultMessageNotificationLevel,
        "explicit_content_filter": enums.ExplicitContentFilterLevel,
        "mfa_level": enums.MFALevel,
        "roles": Role,
        "application_id": Snowflake,
        "system_channel_id": Snowflake,
        "system_channel_flags": bitfields.SystemChannelFlags,
        "rules_channel_id": Snowflake,
        "public_updates_channel_id": Snowflake,
        "safety_updates_channel_id": Snowflake,
        "widget_channel_id": Snowflake,
        "stickers": Sticker,
        "emojis": Emoji,
        "premium_tier": enums.PremiumTier,
        "incidents_data": IncidentsData,
        "nsfw_level": enums.AgeRestrictionLevel,
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

    def banner_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.AnimatedFormat | None = None,
    ) -> str | None:
        """The URL of the guild's icon."""
        if self.banner is None:
            return None
        return cdn.guild_banner(
            guild_id=self.id,
            hash=self.banner,
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
