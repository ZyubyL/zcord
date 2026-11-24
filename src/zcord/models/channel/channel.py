from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from src.zcord.missing import MISSING
from src.zcord.models.user.user import User
from zcord import bitfields, enums
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Channel(Model):
    id: Snowflake
    """The ID of this channel."""

    type: enums.ChannelType
    """The type of channel."""

    guild_id: Snowflake | MISSING = MISSING
    """The ID of the guild.

    Notes:
        May be missing for some channel objects received over gateway \
        guild dispatches.
    """

    position: int | MISSING = MISSING
    """Sorting position of the channel."""

    permission_overwrites: tuple[Overwrite, ...] | MISSING = MISSING
    """Explicit permission overwrites for members and roles."""

    name: str | None | MISSING = MISSING
    """The name of the channel."""

    topic: str | None | MISSING = MISSING
    """The channel topic."""

    nsfw: bool | MISSING = MISSING
    """Whether the channel is age-restricted."""

    last_message_id: Snowflake | None | MISSING = MISSING
    """The ID of the last message sent in this channel.

    Notes:
        May not point to an existing or valid message or thread.
    """

    bitrate: int | MISSING = MISSING
    """The bitrate (in bits per second) of the voice channel."""

    user_limit: int | MISSING = MISSING
    """The user limit of the voice channel."""

    rate_limit_per_user: int | MISSING = MISSING
    """Amount of seconds a user has to wait before sending another message.

    Notes:
        Bots, as well as users with the permission `BYPASS_SLOWMODE`, \
        are unaffected.
    """

    recipients: tuple[User, ...] | MISSING = MISSING
    """The recipients of the DM."""

    icon: str | None | MISSING = MISSING
    """Icon hash of the group DM."""

    owner_id: Snowflake | MISSING = MISSING
    """ID of the creator of the group DM or thread."""

    application_id: Snowflake | None | MISSING = MISSING
    """Application ID associated with the channel.

    For group DMs, this is the application that created the group."""

    managed: bool | MISSING = MISSING
    """For group DM channels: whether the channel is managed \
    by an application via the `gdm.join` OAuth2 scope."""

    parent_id: Snowflake | None | MISSING = MISSING
    """For guild channels: ID of the parent category for a channel \
    (each parent category can contain up to 50 channels).

    For threads: ID of the text channel this thread was created."""

    last_pin_timestamp: datetime | None | MISSING = MISSING
    """When the last pinned message was pinned.

    Notes:
        This may be [`None`][] in events such as `GUILD_CREATE`
        when a message is not pinned.
    """

    rtc_region: str | None | MISSING = MISSING
    """Voice region id for the voice channel, \
    automatic when set to [`None`][]."""

    video_quality_mode: enums.VideoQualityMode | MISSING = MISSING
    """The camera video quality mode of the voice channel.

    Notes:
        This will be \
        [`enums.VideoQualityMode.AUTO`][zcord.enums.VideoQualityMode.AUTO] \
        when not present.
    """

    message_count: int | MISSING = MISSING
    """Number of messages \
    (not including the initial message or deleted messages) in a thread."""

    member_count: int | MISSING = MISSING
    """An approximate count of users in a thread, stops counting at `50`."""

    thread_metadata: ThreadMetadata | MISSING = MISSING
    """Thread-specific fields not needed by other channels."""

    member: ThreadMember | MISSING = MISSING
    """Thread member object for the current user, \
    if they have joined the thread, only included on certain API endpoints."""

    default_auto_archive_duration: int | MISSING = MISSING
    """Default duration, copied onto newly created threads, in minutes, \
    threads will stop showing in the channel list after the specified period \
    of inactivity, can be set to: `60`, `1440`, `4320`, `10080`."""

    permissions: str | MISSING = MISSING
    """Computed permissions for the invoking user in the channel, \
    including overwrites, only included when part of the resolved data \
    received on an interaction.

    Notes:
        This does not include implicit permissions, \
        which may need to be checked separately.
    """

    app_permissions: str | MISSING = MISSING
    """Computed permissions for the bot user in the channel, \
    including overwrites, only included when part of the resolved data \
    received on an interaction.

    Notes:
        This does not include implicit permissions, \
        which may need to be checked separately.
    """

    flags: bitfields.ChannelFlags | MISSING = MISSING
    """Channel flags combined as a bitfield."""

    total_message_sent: int | MISSING = MISSING
    """Number of messages ever sent in a thread, \
    it's similar to message_count on message creation, \
    but will not decrement the number when a message is deleted."""

    available_tags: tuple[Tag, ...] | MISSING = MISSING
    """The set of tags that can be used in a `GUILD_FORUM` or a `GUILD_MEDIA` \
    channel."""

    applied_tags: tuple[Snowflake, ...] | MISSING = MISSING
    """The IDs of the set of tags that have been applied to a thread \
    in a `GUILD_FORUM` or a `GUILD_MEDIA` channel."""

    default_reaction_emoji: DefaultReaction | None | MISSING = MISSING
    """The emoji to show in the add reaction button on a thread \
    in a `GUILD_FORUM` or a `GUILD_MEDIA` channel."""

    default_thread_rate_limit_per_user: int | MISSING = MISSING
    """The initial rate_limit_per_user to set on newly created threads \
    in a channel.

    Notes:
        This field is copied to the thread at creation time \
        and does not live update.
    """

    default_sort_order: enums.DefaultSortOrderType | None | MISSING = MISSING
    """The default sort order type used to order posts \
    in `GUILD_FORUM` and `GUILD_MEDIA` channels.

    Notes:
        Defaults to [`None`][], which indicates a preferred sort order \
        hasn't been set by a channel admin.
    """

    default_forum_layout: enums.DefaultForumLayoutType | MISSING = MISSING
    """The default forum layout view used to display posts \
    in `GUILD_FORUM` channels.

    Notes:
        Defaults to 0, which indicates a layout view has not been set \
        by a channel admin.
    """

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.ChannelType,
        "guild_id": Snowflake,
        "permission_overwrites": Overwrite,
        "last_message_id": Snowflake,
        "recipients": User,
        "owner_id": Snowflake,
        "application_id": Snowflake,
        "parent_id": Snowflake,
        "last_pin_timestamp": datetime.fromisoformat,
        "video_quality_mode": enums.VideoQualityMode,
        "thread_metadata": ThreadMetadata,
        "member": ThreadMember,
        "flags": bitfields.ChannelFlags,
        "available_tags": Tag,
        "applied_tags": Snowflake,
        "default_reaction_emoji": DefaultReaction,
        "default_sort_order": enums.DefaultSortOrderType,
        "default_forum_layout": enums.DefaultForumLayoutType,
    }
