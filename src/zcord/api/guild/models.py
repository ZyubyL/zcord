from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar, Literal

from zcord import bitfields, cdn, enums, types
from zcord.api.channel.models import Channel
from zcord.api.emoji.models import Emoji
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class PromptOption(Model):
    id: Snowflake
    """ID of the prompt option."""

    channel_ids: tuple[Snowflake, ...]
    """IDs for channels a member is added to when the option is selected."""

    role_ids: tuple[Snowflake, ...]
    """IDS for roles assigned to a member when the option is selected."""

    emoji_id: Snowflake
    """Emoji ID of the option."""

    emoji_animated: bool
    """Whether the emoji is animated."""

    title: str
    """Title of the option."""

    description: str | None
    """Description of the option."""

    emoji: Emoji | MISSING = MISSING
    """Emoji of the option."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "channel_ids": Snowflake,
        "role_ids": Snowflake,
        "emoji_id": Snowflake,
        "emoji": Emoji,
    }


@dataclass(frozen=True, slots=True)
class OnboardingPrompt(Model):
    id: Snowflake
    """ID of the prompt."""

    type: enums.PromptType
    """Type of prompt."""

    options: tuple[PromptOption, ...]
    """Options available within the prompt."""

    title: str
    """Title of the prompt."""

    single_select: bool
    """Whether users are limited to selecting one option for the prompt."""

    required: bool
    """Whether the prompt is required before a user completes the \
    onboarding flow."""

    in_onboarding: bool
    """Whether the prompt is present in the onboarding flow.

    If this is [`False`][], the prompt will only appear in the \
    `Channels & Roles` tab."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.PromptType,
        "options": PromptOption,
    }


@dataclass(frozen=True, slots=True)
class GuildOnboarding(Model):
    guild_id: Snowflake
    """ID of the guild this onboarding is part of."""

    prompts: tuple[OnboardingPrompt, ...]
    """Prompts shown during onboarding and in customize community."""

    default_channel_ids: tuple[Snowflake, ...]
    """Channel IDs that members get opted into automatically."""

    enabled: bool
    """Whether onboarding is enabled in the guild."""

    mode: enums.OnboardingMode
    """Current mode of onboarding."""

    _transforms: ClassVar[dict[str, Any]] = {
        "guild_id": Snowflake,
        "prompts": OnboardingPrompt,
        "default_channel_ids": Snowflake,
        "mode": enums.OnboardingMode,
    }


@dataclass(frozen=True, slots=True)
class WelcomeScreenChannel(Model):
    channel_id: Snowflake
    """The channel's ID."""

    description: str
    """The description shown for the channel."""

    emoji_id: Snowflake | None = None
    """The emoji ID, if the emoji is custom."""

    emoji_name: str | None = None
    """The emoji name if custom, the unicode character if standard, \
    or [`None`][] if no emoji is set."""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
        "emoji_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class WelcomeScreen(Model):
    welcome_channels: tuple[WelcomeScreenChannel, ...]
    """The channels shown in the welcome screen."""

    description: str | None = None
    """The server description shown in the welcome screen."""

    _transforms: ClassVar[dict[str, Any]] = {
        "welcome_channels": WelcomeScreenChannel,
    }


@dataclass(frozen=True, slots=True)
class Ban(Model):
    reason: str | None
    """The reason for the ban."""

    user: User
    """The banned user."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user": User,
    }


@dataclass(frozen=True, slots=True)
class GuildWidget(Model):
    id: Snowflake
    """Guild ID."""

    name: str
    """Guild name."""

    instant_invite: str | None
    """Instant invite for the guilds specified widget invite channel."""

    channels: tuple[Channel, ...]
    """Voice and stage channels which are accessible by @everyone."""

    members: tuple[User, ...]
    """Special widget user objects that includes users presence."""

    presence_count: int
    """Number of online member in this guild."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "channels": Channel,
        "members": User,
    }


@dataclass(frozen=True, slots=True)
class GuildWidgetSettings(Model):
    enabled: bool
    """Whether the widget is enabled."""

    channel_id: Snowflake
    """The widget channel ID."""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
    }


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


@dataclass(frozen=True, slots=True)
class IntegrationApplication(Model):
    id: Snowflake
    """The ID of the app."""

    name: str
    """The name of the app."""

    description: str
    """The description of the app."""

    icon: str | None = None
    """The icon hash of the app."""

    bot: User | MISSING = MISSING
    """The bot associated with this application."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "bot": User,
    }

    def icon_url(
        self,
        *,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The application icon URL if available."""
        if not self.icon:
            return None
        return cdn.application_icon_cover(
            app_id=self.id,
            hash=self.icon,
            size=size,
            format=format,
        )


@dataclass(frozen=True, slots=True)
class IntegrationAccount(Model):
    id: str
    """ID of the account."""

    name: str
    """Name of the account."""


@dataclass(frozen=True, slots=True)
class Integration(Model):
    id: Snowflake
    """Integration ID."""

    name: str
    """Integration name."""

    type: Literal["twitch", "youtube", "discord", "guild_subscription"]
    """Integration type."""

    enabled: bool
    """Is this integration enabled."""

    account: IntegrationAccount
    """Integration account information."""

    syncing: bool | MISSING = MISSING
    """Is this integration syncing."""

    role_id: Snowflake | MISSING = MISSING
    """ID that this integration uses for "subscribers"."""

    enable_emoticons: bool | MISSING = MISSING
    """Whether emoticons should be synced for this integration."""

    expire_behavior: enums.IntegrationExpireBehavior | MISSING = MISSING
    """The behavior of expiring subscribers."""

    expire_grace_period: int | MISSING = MISSING
    """The grace period (in days) before expiring subscribers."""

    user: User | MISSING = MISSING
    """User for this integration."""

    synced_at: datetime | MISSING = MISSING
    """When this integration was last synced."""

    subscriber_count: int | MISSING = MISSING
    """How many subscribers this integration has."""

    revoked: bool | MISSING = MISSING
    """Has this integration been revoked."""

    application: IntegrationApplication | MISSING = MISSING
    """The bot/OAuth2 appliction for Discord integration."""

    # NOTE: Maybe OAuth2 Scopes
    # https://docs.discord.com/developers/topics/oauth2#shared-resources-oauth2-scopes
    scopes: tuple[str, ...] | MISSING = MISSING
    """The scopes the application has been authorized for."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "account": IntegrationAccount,
        "role_id": Snowflake,
        "expire_behavior": enums.IntegrationExpireBehavior,
        "user": User,
        "synced_at": datetime.fromisoformat,
        "application": IntegrationApplication,
    }


@dataclass(frozen=True, slots=True)
class IncidentsData(Model):
    """The incidents data for the Guild."""

    invites_disabled_until: datetime | None
    """When invites get enabled again."""

    dms_disabled_until: datetime | None
    """When direct messages get enabled again."""

    dm_spam_detected_at: datetime | None | MISSING = MISSING
    """When the DM spam was detected."""

    raid_detected_at: datetime | None | MISSING = MISSING
    """When the raid was detected."""

    _transforms: ClassVar[dict[str, Any]] = {
        "invites_disabled_until": datetime.fromisoformat,
        "dms_disabled_until": datetime.fromisoformat,
        "dm_spam_detected_at": datetime.fromisoformat,
        "raid_detected_at": datetime.fromisoformat,
    }


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


@dataclass(frozen=True, slots=True)
class GuildMember(Model):
    roles: tuple[Snowflake, ...]
    """Tuple of [`Role`][zcord.Role] IDs."""

    deaf: bool
    """Whether the user is deafened in voice channels."""

    mute: bool
    """Whether the user is muted in voice channels."""

    permissions: str
    """Total permissions of the member in the channel, including overwrites, \
    returned when in the interaction object."""

    user: User | MISSING = MISSING
    """The user this guild member represents."""

    nick: str | None | MISSING = MISSING
    """This user's guild nickname."""

    avatar: str | None | MISSING = MISSING
    """The member's guild avatar hash."""

    bannner: str | None | MISSING = MISSING
    """The member's guild banner hash."""

    joined_at: datetime | None = None
    """When the user joined the guild."""

    premium_since: datetime | None | MISSING = MISSING
    """When the user started boosting the guild."""

    flags: bitfields.GuildMemberFlags = bitfields.GuildMemberFlags.DEFAULT
    """This guild member's flags."""

    pending: bool | MISSING = MISSING
    """Whether the user has not yet passed the guild's membership screening \
    requirement."""

    communication_diabled_until: datetime | None | MISSING = MISSING
    """When the user's timeout will expire and the user will be able to \
    communicate in the guild again, [`None`][] or time in the past if \
    the user is not timed out."""

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """Data for the member's guild avatar decoration."""

    collectibles: Collectibles | None | MISSING = MISSING
    """Data for the member's collectibles."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user": User,
        "roles": Snowflake,
        "joined_at": datetime.fromisoformat,
        "premium_since": datetime.fromisoformat,
        "flags": bitfields.GuildMemberFlags,
        "communication_diabled_until": datetime.fromisoformat,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
    }
