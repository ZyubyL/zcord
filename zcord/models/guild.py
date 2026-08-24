from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Literal

from zcord import bitfields
from zcord.cdn import CDN
from zcord.enums import (
    ExplicitContentFilterLevel,
    MessageNotificationLevel,
    MFALevel,
    VerificationLevel,
)
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.emoji import Emoji
from zcord.models.role import Role
from zcord.models.snowflake import Snowflake
from zcord.models.sticker import Sticker


@dataclass(frozen=True, slots=True)
class Guild(Model):
    """
    Represent a Discord server.
    """

    id: Snowflake
    """
    The ID of the guild.
    """

    name: str
    """
    The name of the guild.

    **Notes**: 2-100 characters excluding leading and trailing whitespaces.
    """

    icon: str | None
    """
    The icon hash of the guild.
    """

    splash: str | None
    """
    The splash hash of the guild.
    """

    discovery_splash: str | None
    """
    The discovery splash hash of the guild with "DISCOVERABLE" feature.
    """

    owner_id: Snowflake
    """
    The ID of the owner.
    """

    afk_channel_id: Snowflake | None
    """
    The ID of the AFK channel.
    """

    afk_timeout: int
    """
    AFK timeout, in seconds.
    """

    verification_level: VerificationLevel
    """
    Verification level of the guild.
    """

    default_message_notifications: MessageNotificationLevel
    """
    Default message notification level.
    """

    explicit_content_filter: ExplicitContentFilterLevel
    """
    Explicit content filter level.
    """

    roles: tuple[Role, ...]
    """
    A list of roles in the guild.
    """

    emojis: tuple[Emoji, ...]
    """
    A list of custom guild emoji.
    """

    features: tuple[Any]
    """
    A list of enabled guild features.
    """

    mfa_level: MFALevel
    """
    Required MFA level for the guild.
    """

    application_id: Snowflake | None
    """
    Application ID of the guild creator if it's bot-created.
    """

    system_channel_id: Snowflake | None
    """
    The ID of the channel where system messages are sent.
    """

    system_channel_flags: bitfields.SystemChannelFlags
    """
    System channel flags.
    """

    rules_channel_id: Snowflake | None
    """
    The ID of the rules and/or guidelines channel.
    """

    vanity_url_code: str | None
    """
    The vanity url code for the guild.
    """

    description: str | None
    """
    The description of the guild.
    """

    banner: str | None
    """
    The banner hash of the guild.
    """

    premium_tier: int
    """
    Guild boost level.
    """

    preferred_locale: str
    """
    The preferred locale of the Community guild.
    """

    public_updates_channel_id: Snowflake | None
    """
    The ID of the channel where admins and moderators of Community
    guilds receive notices from Discord.
    """

    nsfw_level: int
    """
    Guild age-restriction level.
    """

    premium_progress_bar_enabled: bool
    """
    Whether the guild has the boost progress bar enabled.
    """

    safety_alerts_channel_id: Snowflake | None
    """
    The ID of the channel where admins and moderators of Community
    guilds receive safety alerts from Discord.
    """

    incidents_data: Any | None
    """
    The incidents data of this guild.
    """

    icon_hash: str | None | MISSING = MISSING
    """
    The icon hash of the guild when in a guild template.
    """

    owner: bool | MISSING = MISSING
    """
    If the user is the owner of the guild.
    """

    permissions: str | MISSING = MISSING
    """
    Total permissions for the user in the guild.
    """

    widget_enabled: bool | MISSING = MISSING
    """
    Whether the guild widget is enabled.
    """

    widget_channel_id: Snowflake | None | MISSING = MISSING
    """
    The channel ID that the widget will generate an invite to.
    """

    max_presences: int | None | MISSING = MISSING
    """
    The maximum number of presences for the guild.
    """

    max_members: int | None | MISSING = MISSING
    """
    The maximum number of members for the guild.
    """

    premium_subsription_count: int | MISSING = MISSING
    """
    The number of boosts this guild currently has.
    """

    max_video_channel_users: int | MISSING = MISSING
    """
    The maximum amount of users in a video channel.
    """

    max_stage_video_channel_users: int | MISSING = MISSING
    """
    The maximum amount of users in a stage video channel.
    """

    approximate_member_count: int | MISSING = MISSING
    """
    Approximate number of members in this guild.
    """

    approximate_presence_count: int | MISSING = MISSING
    """
    Approximate number of non-offline members in this guild.
    """

    welcome_screen: Any | MISSING = MISSING
    """
    The welcome screen of a Community guild shown to new members.
    """

    stickers: tuple[Sticker, ...] | MISSING = MISSING
    """
    A list of custom guild stickers.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "owner_id": Snowflake,
        "afk_channel_id": Snowflake,
        "verification_level": VerificationLevel,
        "default_message_notifications": MessageNotificationLevel,
        "explicit_content_filter": ExplicitContentFilterLevel,
        "mfa_level": MFALevel,
        "roles": Role,
        "application_id": Snowflake,
        "system_channel_id": Snowflake,
        "system_channel_flags": bitfields.SystemChannelFlags,
        "rules_channel_id": Snowflake,
        "public_updates_channel_id": Snowflake,
        "safety_alerts_channel_id": Snowflake,
        "widget_channel_id": Snowflake,
        "stickers": Sticker,
        "emojis": Emoji,
    }

    def icon_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the guild's icon.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.icon_hash is None or self.icon_hash is MISSING:
            return None
        return CDN.guild_icon(
            guild_id=self.id,
            hash=self.icon_hash,
            size=size,
            format=format,
        )

    def banner_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the guild's icon.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.banner is None:
            return None
        return CDN.guild_banner(
            guild_id=self.id,
            hash=self.banner,
            size=size,
            format=format,
        )
