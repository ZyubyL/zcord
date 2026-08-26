from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, ClassVar

from zcord import bitfields, enums, errors
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.default_reaction import DefaultReaction
from zcord.models.snowflake import Snowflake
from zcord.models.thread_member import ThreadMember
from zcord.models.thread_metadata import ThreadMetadata
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.message import Message
    from zcord.state import ConnectionState


@dataclass(frozen=True, slots=True)
class Channel(Model):
    """
    Represent a Discord server or DM channel.
    """

    id: Snowflake | MISSING = MISSING
    """
    The ID of the channel.
    """

    type: enums.ChannelType | MISSING = MISSING
    """
    The channel type.
    """

    guild_id: Snowflake | MISSING = MISSING
    """
    The guild ID the message belongs to.
    """

    position: int | MISSING = MISSING
    """
    The sorting position of the channel.
    """

    permission_overwrites: list | MISSING = MISSING
    """
    A list of explicit permission overwrites for members and roles.
    """

    name: str | None | MISSING = MISSING
    """
    The name of the channel.

    **Notes**: Can only be in 1-100 characters range.
    """

    topic: str | None | MISSING = MISSING
    """
    The channel's topic.

    **Notes**:
        For most `ChannelType`, it can be up to 1024
        characters long. Except `GUILD_FORUM` which can be up to
        4096 characters.
    """

    nsfw: bool | MISSING = MISSING
    """
    Whether the channel is age-restricted.
    """

    last_message_id: Snowflake | None | MISSING = MISSING
    """
    The ID of the last message sent in this channel.
    """

    bitrate: int | MISSING = MISSING
    """
    The bit per second of the voice channel.
    """

    user_limit: int | MISSING = MISSING
    """
    The user limit of the voice channel.
    """

    rate_limit_per_user: int | MISSING = MISSING
    """
    The channel slowmode in seconds. This ranges from 0-21600.
    """

    recipients: tuple[User, ...] | MISSING = MISSING
    """
    The recipients of the DM.
    """

    icon: str | None | MISSING = MISSING
    """
    The icon hash of the Group DM.
    """

    owner_id: Snowflake | MISSING = MISSING
    """
    The ID of the Group DM or a thread.
    """

    application_id: Snowflake | MISSING = MISSING
    """
    The app ID of the Group DM if it's created by a bot.
    """

    managed: bool | MISSING = MISSING
    """
    Whether the channel is managed.
    """

    parent_id: Snowflake | None | MISSING = MISSING
    """
    For guild channels, it's the parent category ID.
    For threads, it's the text channel ID.
    """

    last_pin_timestamp: datetime | None | MISSING = MISSING
    """
    When the last pinned message was pinned.
    """

    rtc_region: str | None | MISSING = MISSING
    """
    ID of the region of the voice channel. Automatic when set to None.
    """

    video_quality_mode: int | MISSING = MISSING
    """
    The camera video quality mode of the voice channel.
    `1` when not present.
    """

    message_count: int | MISSING = MISSING
    """
    Number of messages[^1] in a thread.

    [^1]:Can be inaccurate if the thread was created before July 1st, 2022.
    """

    member_count: int | MISSING = MISSING
    """
    Approximate count of users[^1] in a thread.

    [^1]: Stop counting at 50.
    """

    thread_metadata: ThreadMetadata | MISSING = MISSING
    """
    Thread specific fields.
    """

    member: ThreadMember | MISSING = MISSING
    """
    Thread member object for the current user, if they have joined the thread.
    """

    default_auto_archive_duration: int | MISSING = MISSING
    """
    Default duration for threads to be auto archived (in minutes).

    **Notes**: Can be set to 60, 1440, 4320, 10080.
    """

    permissions: str | MISSING = MISSING
    """
    Computed permissions for the invoking user in the channel, including
    overwrites.
    """

    flags: bitfields.ChannelFlags | MISSING = MISSING
    """
    Channel flags combined as a bitfield.
    """

    total_message_sent: int | MISSING = MISSING
    """
    Number of messages ever sent[^1] in a thread.

    [^1]: Unlike `message_count`, the value won't
    decrease when a message is deleted.
    """

    available_tags: tuple | MISSING = MISSING
    """
    The set of tags that can be used in a `GUILD_FORUM` channel.
    """

    applied_tags: tuple[Snowflake, ...] | MISSING = MISSING
    """
    The IDs of the set of tags that have been applied to a thread in a
    `GUILD_FORUM` channel.
    """

    default_reaction_emoji: DefaultReaction | None | MISSING = MISSING
    """
    The emoji to show in the add reaction button on a thread in a
    `GUILD_FORUM` channel.
    """

    default_thread_rate_limit_per_user: int | MISSING = MISSING
    """
    The initial `rate_limit_per_user` to set on newly created threads
    in a channel.
    """

    default_sort_order: int | None | MISSING = MISSING
    """
    The default sort order type used to order posts in `GUILD_FORUM` channel.
    """

    default_forum_layout: int | MISSING = MISSING
    """
    The default forum layout view used to display posts in `GUILD_FORUM`
    channel.
    """

    _state: ClassVar[ConnectionState | MISSING] = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": enums.ChannelType,
        "guild_id": Snowflake,
        "last_message_id": Snowflake,
        "recipients": User,
        "owner_id": Snowflake,
        "application_id": Snowflake,
        "parent_id": Snowflake,
        "last_pin_timestamp": datetime.fromisoformat,
        "flags": bitfields.ChannelFlags,
        "applied_tags": Snowflake,
        "thread_metadata": ThreadMetadata,
        "default_reaction_emoji": DefaultReaction,
        "member": ThreadMember,
    }

    async def send(self, message: Message) -> Message:
        """
        Send a message to this channel.
        """
        if self.id is MISSING:
            raise errors.ZcordError(
                "Cannot send a message to a channel without an ID"
            )
        if message.id is not MISSING:
            raise errors.ZcordError(
                "Cannot send a message that already has an ID"
            )
        assert self._state is not MISSING
        return await self._state.send_message(channel_id=self, message=message)
