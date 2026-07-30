from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.enums.message import (
    MessageActivityType,
    MessageReferenceType,
    MessageType,
)
from zcord.missing import MISSING
from zcord.models.application import Application
from zcord.models.attachment import Attachment
from zcord.models.base import ZcordModel
from zcord.models.channel import Channel
from zcord.models.embed import Embed
from zcord.models.interaction import InteractionMetadata
from zcord.models.poll import Poll
from zcord.models.reaction import Reaction
from zcord.models.role import Role, RoleSubscriptionData
from zcord.models.shared_client_theme import SharedClientTheme
from zcord.models.snowflake import Snowflake
from zcord.models.sticker import Sticker
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class MessageActivity(ZcordModel):
    """
    Contain info about a [`Message`][zcord.Message]'s activity.

    Attributes:
        type:
            The type of activity.
        party_id:
            The party ID from a Rich presence event.
    """

    type: MessageActivityType
    party_id: str | MISSING = MISSING

    _transforms: ClassVar[dict] = {"type": MessageActivityType}


@dataclass(frozen=True, slots=True)
class MessageReference(ZcordModel):
    """
    Contains the additional data of the referenced message.

    Attributes:
        type:
            The type of reference.
        message_id:
            The ID of the originating message.
        channel_id:
            The ID of the originating message's channnel.
        guild_id:
            The ID of the originating messgae's guild.
        fail_if_not_exists:
            Whether to error if the referenced message doesn't exist instead \
            of sending as a normal (non-reply) message
    """

    type: MessageReferenceType = MessageReferenceType.DEFAULT
    message_id: Snowflake | MISSING = MISSING
    channel_id: Snowflake | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    fail_if_not_exists: bool = True  # Maybe I won't need to expose this, idk

    _transforms: ClassVar[dict] = {
        "type": MessageReferenceType,
        "message_id": Snowflake,
        "channel_id": Snowflake,
        "guild_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class MessageSnapshot(ZcordModel):
    """
    The snapshot of a forwarded message.

    Attributes:
        message:
            The forwarded message.
    """

    message: Message


@dataclass(frozen=True, slots=True)
class Message(ZcordModel):
    """Represent a Discord message.

    Attributes:
        id:
            The ID of the message.
        channel_id:
            The ID of the channel the message was sent in.
        author:
            The author of this message.
        content:
            The message content.
        timestamp:
            The timestamp when this message was sent.
        edited_timestamp:
            The timestamp when this message was edited.
        tts:
            Whether this message is a text-to-speech message.
        mention_everyone:
            Whether this message mentions everyone.
        mentions:
            Users mentioned in this message.
        mention_roles:
            Roles mentioned in this message.
        mention_channels:
            Channels mentioned in this message.
        attachments:
            Attached files in this message.
        embeds:
            Embeded contents in this message.
        reactions:
            Reactions to this message.
        pinned:
            Whether this message is pinned.
        webhook_id:
            The webhook's ID if this message was sent via webhook.
        type:
            The type of the message.
        activity:
            Activity object sent via Rich presence related embeds.
        application:
            Partial application object sent via Rich presence related embeds.
        application_id:
            The application ID if this message was sent via an `Interaction`
            or an application-owned webhook.
        flags:
            The message flags combined as a bitfield.
        message_reference:
            The source of the crosspost, channel follow add, pin, or reply
            message.
        message_snapshots:
            The message associated with the `message_reference`. This is a
            minimal subset of fields in a `Message`.
        referenced_message:
            The message associated with the `message_reference`.
        interaction_metadata:
            Message interaction metadata.
        thread:
            The thread that was started from this message.
        components:
            Interactive components in this message.
        sticker_items:
            Stickers in this message.
        position:
            The approximated position of the message in a thread.
        role_subscription_data:
            Data of the subscription if this message is a
            `ROLE_SUBSCRIPTION_PURCHASE` message
        resolved:
            Data for users, members, channels, and roles referenced in
            this message.
        poll:
            A poll.
        call:
            The call associated with this message.
        shared_client_theme:
            The custom client-side theme shared in this message.
    """

    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: datetime
    tts: bool
    mention_everyone: bool
    mentions: list[User]
    mention_roles: list[Snowflake]
    attachments: list[Attachment]
    embeds: list[Embed]
    pinned: bool
    type: MessageType
    edited_timestamp: datetime | None = None
    mention_channels: list[Channel] | MISSING = MISSING
    reactions: list[Reaction] | MISSING = MISSING
    webhook_id: Snowflake | MISSING = MISSING
    activity: MessageActivity | MISSING = MISSING
    application: Application | MISSING = MISSING
    application_id: Snowflake | MISSING = MISSING
    flags: int | MISSING = MISSING
    message_reference: MessageReference | MISSING = MISSING
    message_snapshots: list[MessageSnapshot] | MISSING = MISSING
    referenced_message: Message | None | MISSING = MISSING
    interaction_metadata: InteractionMetadata | MISSING = MISSING
    thread: Channel | MISSING = MISSING
    components: list | MISSING = MISSING
    sticker_items: list[Sticker] | MISSING = MISSING
    position: int | MISSING = MISSING
    role_subscription_data: RoleSubscriptionData | MISSING = MISSING
    resolved: Resolved | MISSING = MISSING
    poll: Poll | MISSING = MISSING
    call: Any | MISSING = MISSING
    shared_client_theme: SharedClientTheme | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "channel_id": Snowflake,
        "author": User,
        "timestamp": datetime.fromisoformat,
        "edited_timestamp": datetime.fromisoformat,
        "mentions": User,
        "attachments": Attachment,
        "embeds": Embed,
        "mention_roles": Snowflake,
        "mention_channels": Channel,
        "reactions": Reaction,
        "webhook_id": Snowflake,
        "activity": MessageActivity,
        "application": Application,
        "type": MessageType,
        "application_id": Snowflake,
        "message_reference": MessageReference,
        "message_snapshots": MessageSnapshot,
        "interaction_metadata": InteractionMetadata,
        "thread": Channel,
        "sticker_items": Sticker,
        "role_subscription_data": RoleSubscriptionData,
        "poll": Poll,
        "shared_client_theme": SharedClientTheme,
    }


@dataclass(frozen=True, slots=True)
class Resolved(ZcordModel):
    """
    Resolved data in the [`Message`][].

    Attributes:
        users:
            A dict of user ID to User.
        members:
            A dict of member ID to Member.
        roles:
            A dict of role ID to Role.
        channels:
            A dict of channel ID to Channel.
        messages:
            A dict of message ID to Message.
        attachments:
            A dict of attachment ID to Attachment.
    """

    users: dict[Snowflake, User] | MISSING = MISSING
    members: dict[Snowflake, Any] | MISSING = MISSING
    roles: dict[Snowflake, Role] | MISSING = MISSING
    channels: dict[Snowflake, Channel] | MISSING = MISSING
    messages: dict[Snowflake, Message] | MISSING = MISSING
    attachments: dict[Snowflake, Attachment] | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "users": dict[Snowflake, User],
        "roles": dict[Snowflake, Role],
        "channels": dict[Snowflake, Channel],
        "messages": dict[Snowflake, Message],
        "attachments": dict[Snowflake, Attachment],
    }


Message._transforms["referenced_message"] = Message
Message._transforms["resolved"] = Resolved
