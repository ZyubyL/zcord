from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING, Any, ClassVar

from zcord.enums import ChannelType
from zcord.errors import ZcordError
from zcord.flags import ChannelFlags
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.message import Message
    from zcord.state import ConnectionState


@dataclass(frozen=True, slots=True)
class Channel(Model):
    """
    Represent a Discord server or DM channel.

    Attributes:
        id:
            The ID of the channel.
        type:
            The channel type.
        guild_id:
            The guild id the message belongs to.
        position:
            The sorting position of the channel.
        permission_overwrites:
            A list of explicit permission overwrites for members and roles.
        name:
            The name of the channel.

            **Notes**: Can only be in 1-100 characters range.
        topic:
            The channel's topic.

            **Notes**: For most `ChannelType`, it can be up to 1024
            characters long. Except `GUILD_FORUM` which can be up to
            4096 characters.
        nsfw:
            Whether the channel is age-restricted.
        last_message_id:
            The ID of the last message sent in this channel.
        bitrate:
            The bit per second of the voice channel.
        user_limit:
            The user limit of the voice channel.
        rate_limit_per_user:
            The channel slowmode in seconds. This ranges from 0-21600.
        recipients:
            The recipients of the DM.
        icon:
            The icon hash of the Group DM.
        owner_id:
            The ID of the Group DM or a thread.
        applicaiton_id:
            The app ID of the Group DM if it's created by a bot.
        managed:
            Whether the channel is managed.
        parent_id:
            For guild channels, it's the parent category ID.
            For threads, it's the text channel ID.
        last_pin_timestamp:
            When the last pinned message was pinned.
        rtc_region:
            ID of the region of the voice channel. Automatic when set to None.
        video_quality_mode:
            The camera video quality mode of the voice channel.
            `1` when not present.
        message_count:
            Number of messages in a thread.

            **Notes**: Can be inaccurate if the thread was created before
            July 1st, 2022.
        member_count:
            Approximate count of users in a thread.

            **Notes**: stop counting at 50.
        thread_metadata:
            Thread specific fields.
        member:
            Thread member object for the current user, if they have joined the
            thread.
        default_auto_archive_duration:
            Default duration for threads to be auto archived (in minutes).

            **Notes**: Can be set to 60, 1440, 4320, 10080.
        permissions:
            Computed permissions for the invoking user in the channel, including
            overwrites.
        flags:
            Channel flags combined as a bitfield.
        total_message_sent:
            Number of messages ever sent in a thread.

            **Notes**: Unlike `message_count`, the value won't
            decrease when a message is deleted.
        available_tags:
            The set of tags that can be used in a `GUILD_FORUM` channel.
        applied_tags:
            The IDs of the set of tags that have been applied to a thread in a
            `GUILD_FORUM` channel.
        default_reaction_emoji:
            The emoji to show in the add reaction button on a thread in a
            `GUILD_FORUM` channel.
        default_thread_rate_limit_per_user:
            The initial `rate_limit_per_user` to set on newly created threads
            in a channel.
        default_sort_order:
            The default sort order type used to order posts in `GUILD_FORUM`
            channel.
        default_forum_layout:
            The default forum layout view used to display posts in `GUILD_FORUM`
            channel.
    """

    id: Snowflake | MISSING = MISSING
    type: ChannelType | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    position: int | MISSING = MISSING
    permission_overwrites: list | MISSING = MISSING
    name: str | None | MISSING = MISSING
    topic: str | None | MISSING = MISSING
    nsfw: bool | MISSING = MISSING
    last_message_id: Snowflake | None | MISSING = MISSING
    bitrate: int | MISSING = MISSING
    user_limit: int | MISSING = MISSING
    rate_limit_per_user: int | MISSING = MISSING
    recipients: tuple[User, ...] | MISSING = MISSING
    icon: str | None | MISSING = MISSING
    owner_id: Snowflake | MISSING = MISSING
    application_id: Snowflake | MISSING = MISSING
    managed: bool | MISSING = MISSING
    parent_id: Snowflake | None | MISSING = MISSING
    last_pin_timestamp: datetime | None | MISSING = MISSING
    rtc_region: str | None | MISSING = MISSING
    video_quality_mode: int | MISSING = MISSING
    message_count: int | MISSING = MISSING
    member_count: int | MISSING = MISSING
    thread_metadata: Any | MISSING = MISSING
    member: Any | MISSING = MISSING
    default_auto_archive_duration: int | MISSING = MISSING
    permissions: str | MISSING = MISSING
    flags: ChannelFlags | MISSING = MISSING
    total_message_sent: int | MISSING = MISSING
    available_tags: tuple | MISSING = MISSING
    applied_tags: tuple[Snowflake, ...] | MISSING = MISSING
    default_reaction_emoji: Any | None | MISSING = MISSING
    default_thread_rate_limit_per_user: int | MISSING = MISSING
    default_sort_order: int | None | MISSING = MISSING
    default_forum_layout: int | MISSING = MISSING

    _state: ClassVar[ConnectionState | MISSING] = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": ChannelType,
        "guild_id": Snowflake,
        "last_message_id": Snowflake,
        "recipients": User,
        "owner_id": Snowflake,
        "application_id": Snowflake,
        "parent_id": Snowflake,
        "last_pin_timestamp": datetime.fromisoformat,
        "flags": ChannelFlags,
        "applied_tags": Snowflake,
    }

    async def send(self, message: Message) -> Message:
        """*|coro|*

        Send a message to this channel.
        """
        if self.id is MISSING:
            raise ZcordError("Cannot send a message to a channel without an ID")
        if message.id is not MISSING:
            raise ZcordError("Cannot send a message that already has an ID")
        assert self._state is not MISSING
        return await self._state.send_message(channel_id=self, message=message)
