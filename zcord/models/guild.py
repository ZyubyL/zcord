from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.enums import (
    ExplicitContentFilterLevel,
    MessageNotificationLevel,
    MFALevel,
    VerificationLevel,
)
from zcord.flags import SystemChannelFlags
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.role import Role
from zcord.models.snowflake import Snowflake
from zcord.models.sticker import Sticker


@dataclass(frozen=True, slots=True)
class Guild(ZcordModel):
    """
    Represent a Discord server.

    Attributes:
        id:
            The ID of the guild.
        name:
            The name of the guild.

            **Notes**: 2-100 characters excluding leading and trailing
            whitespaces.
        icon:
            The icon hash of the guild.
        icon_hash:
            The icon hash of the guild when in a guild template.
        splash:
            The splash hash of the guild.
        discovery_splash:
            The discovery splash hash of the guild with "DISCOVERABLE" feature.
        owner:
            If the user is the owner of the guild.
        owner_id:
            The ID of the owner.
        permissions:
            Total permissions for the user in the guild.
        afk_channel_id:
            The ID of the AFK channel.
        afk_timeout:
            AFK timeout, in seconds.
        widget_enabled:
            Whether the guild widget is enabled.
        widget_channel_id:
            The channel ID that the widget will generate an invite to.
        verification_level:
            Verification level of the guild.
        default_message_notifications:
            Default message notification level.
        explicit_content_filter:
            Explicit content filter level.
        roles:
            A list of roles in the guild.
        emojis:
            A list of custom guild emoji.
        features:
            A list of enabled guild features.
        mfa_level:
            Required MFA level for the guild.
        application_id:
            Application ID of the guild creator if it's bot-created.
        system_channel_id:
            The ID of the channel where system messages are sent.
        system_channel_flags:
            System channel flags.
        rules_channel_id:
            The ID of the rules and/or guidelines channel.
        max_presences:
            The maximum number of presences for the guild.
        max_members:
            The maximum number of members for the guild.
        vanity_url_code:
            The vanity url code for the guild.
        description:
            The description of the guild.
        banner:
            The banner hash of the guild.
        premium_tier:
            Guild boost level.
        premium_subscription_count:
            The number of boosts this guild currently has.
        preferred_locale:
            The preferred locale of the Community guild.
        public_updates_channel_id:
            The ID of the channel where admins and moderators of Community
            guilds receive notices from Discord.
        max_video_channel_users:
            The maximum amount of users in a video channel.
        max_stage_video_channel_users:
            The maximum amount of users in a stage video channel.
        approximate_member_count:
            Approximate number of members in this guild.
        approximate_presence_count:
            Approximate number of non-offline members in this guild.
        welcome_screen:
            The welcome screen of a Community guild shown to new members.
        nsfw_level:
            Guild age-restriction level.
        stickers:
            A list of custom guild stickers.
        premium_progress_bar_enabled:
            Whether the guild has the boost progress bar enabled.
        safety_alerts_channel_id:
            The ID of the channel where admins and moderators of Community
            guilds receive safety alerts from Discord.
        incidents_data:
            The incidents data of this guild.
    """

    id: Snowflake
    name: str
    icon: str | None
    splash: str | None
    discovery_splash: str | None
    owner_id: Snowflake
    afk_channel_id: Snowflake | None
    afk_timeout: int
    verification_level: VerificationLevel
    default_message_notifications: MessageNotificationLevel
    explicit_content_filter: ExplicitContentFilterLevel
    roles: tuple[Role, ...]
    emojis: tuple[Any]
    features: tuple[Any]
    mfa_level: MFALevel
    application_id: Snowflake | None
    system_channel_id: Snowflake | None
    system_channel_flags: SystemChannelFlags
    rules_channel_id: Snowflake | None
    vanity_url_code: str | None
    description: str | None
    banner: str | None
    premium_tier: int
    preferred_locale: str
    public_updates_channel_id: Snowflake | None
    nsfw_level: int
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: Snowflake | None
    incidents_data: Any | None
    icon_hash: str | None | MISSING = MISSING
    owner: bool | MISSING = MISSING
    permissions: str | MISSING = MISSING
    widget_enabled: bool | MISSING = MISSING
    widget_channel_id: Snowflake | None | MISSING = MISSING
    max_presences: int | None | MISSING = MISSING
    max_members: int | None | MISSING = MISSING
    premium_subsription_count: int | MISSING = MISSING
    max_video_channel_users: int | MISSING = MISSING
    max_stage_video_channel_users: int | MISSING = MISSING
    approximate_member_count: int | MISSING = MISSING
    approximate_presence_count: int | MISSING = MISSING
    welcome_screen: Any | MISSING = MISSING
    stickers: tuple[Sticker, ...] | MISSING = MISSING

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
        "system_channel_flags": SystemChannelFlags,
        "rules_channel_id": Snowflake,
        "public_updates_channel_id": Snowflake,
        "safety_alerts_channel_id": Snowflake,
        "widget_channel_id": Snowflake,
        "stickers": Sticker,
    }
