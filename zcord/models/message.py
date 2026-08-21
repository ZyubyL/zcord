from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import TYPE_CHECKING, Any, ClassVar

from zcord.enums.message import (
    MessageActivityType,
    MessageReferenceType,
    MessageType,
)
from zcord.errors import ZcordError
from zcord.flags import MessageFlags
from zcord.missing import MISSING
from zcord.models.application import Application
from zcord.models.attachment import Attachment
from zcord.models.base import Model
from zcord.models.channel import Channel
from zcord.models.component import Component
from zcord.models.component.action_row import ActionRow
from zcord.models.embed import Embed
from zcord.models.interaction import InteractionMetadata
from zcord.models.poll import Poll
from zcord.models.reaction import Reaction
from zcord.models.role import Role, RoleSubscriptionData
from zcord.models.shared_client_theme import SharedClientTheme
from zcord.models.snowflake import Snowflake
from zcord.models.sticker import Sticker
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.state import ConnectionState


@dataclass(frozen=True, slots=True)
class MessageActivity(Model):
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
class MessageReference(Model):
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
class MessageSnapshot(Model):
    """
    The snapshot of a forwarded message.

    Attributes:
        message:
            The forwarded message.
    """

    message: Message


@dataclass(frozen=True, slots=True)
class Message(Model):
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

    id: Snowflake | MISSING = MISSING
    channel_id: Snowflake | MISSING = MISSING
    author: User | MISSING = MISSING
    content: str | MISSING = MISSING
    timestamp: datetime | MISSING = MISSING
    tts: bool | MISSING = MISSING
    mention_everyone: bool | MISSING = MISSING
    mentions: tuple[User, ...] | MISSING = MISSING
    mention_roles: tuple[Snowflake, ...] | MISSING = MISSING
    attachments: tuple[Attachment, ...] | MISSING = MISSING
    embeds: tuple[Embed, ...] | MISSING = MISSING
    pinned: bool | MISSING = MISSING
    type: MessageType | MISSING = MISSING
    edited_timestamp: datetime | None = None
    mention_channels: tuple[Channel, ...] | MISSING = MISSING
    reactions: tuple[Reaction, ...] | MISSING = MISSING
    webhook_id: Snowflake | MISSING = MISSING
    activity: MessageActivity | MISSING = MISSING
    application: Application | MISSING = MISSING
    application_id: Snowflake | MISSING = MISSING
    flags: MessageFlags | MISSING = MISSING
    message_reference: MessageReference | MISSING = MISSING
    message_snapshots: tuple[MessageSnapshot, ...] | MISSING = MISSING
    referenced_message: Message | None | MISSING = MISSING
    interaction_metadata: InteractionMetadata | MISSING = MISSING
    thread: Channel | MISSING = MISSING
    components: tuple[Component, ...] | MISSING = MISSING
    sticker_items: tuple[Sticker, ...] | MISSING = MISSING
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
        "flags": MessageFlags,
        "message_reference": MessageReference,
        "message_snapshots": MessageSnapshot,
        "interaction_metadata": InteractionMetadata,
        "thread": Channel,
        "components": Component,
        "sticker_items": Sticker,
        "role_subscription_data": RoleSubscriptionData,
        "poll": Poll,
        "shared_client_theme": SharedClientTheme,
    }

    _state: ClassVar[ConnectionState | MISSING] = MISSING

    @classmethod
    def new(
        cls,
        *,
        content: str | MISSING = MISSING,
        attachments: tuple[Attachment, ...]
        | list[Attachment]
        | MISSING = MISSING,
        embeds: tuple[Embed, ...] | list[Embed] | MISSING = MISSING,
        # webhook_id: Snowflake | MISSING = MISSING,
        message_reference: MessageReference | MISSING = MISSING,
        message_snapshots: tuple[MessageSnapshot, ...]
        | list[MessageSnapshot]
        | MISSING = MISSING,
        referenced_message: Message | None | MISSING = MISSING,
        # thread: Channel | MISSING = MISSING,
        components: tuple[Component, ...] | list[Component] | MISSING = MISSING,
        # sticker_items: list[Sticker] | MISSING = MISSING,
        poll: Poll | MISSING = MISSING,
        # call: Any | MISSING = MISSING,
        shared_client_theme: SharedClientTheme | MISSING = MISSING,
    ) -> Message:
        """*|classmethod|*

        Create a new message.

        Raises:
            ValueError:
                - Number of embeds exceeds 10.
                - You can only add ActionRow for now.
                - Number of components exceeds 5.
        """
        return (
            cls(
                message_reference=message_reference,
                referenced_message=referenced_message,
            )
            ._set_message_snapshots(message_snapshots)
            .set_content(content)
            .set_embeds(embeds)
            .set_components(components)
            .set_attachments(attachments)
            .set_poll(poll)
            .set_shared_client_theme(shared_client_theme)
        )

    def _set_message_snapshots(
        self,
        message_snapshots: tuple[MessageSnapshot, ...]
        | list[MessageSnapshot]
        | MISSING,
    ) -> Message:
        if message_snapshots is not MISSING:
            return replace(self, message_snapshots=message_snapshots)
        return self

    def set_content(self, content: str | MISSING = MISSING) -> Message:
        """
        Set the content of the message.
        """
        return replace(self, content=content)

    def set_embeds(
        self, embeds: tuple[Embed, ...] | list[Embed] | MISSING = MISSING
    ) -> Message:
        """
        Set the embeds of the message.

        Raises:
            ValueError:
                Number of embeds exceeds 10.
        """
        m = self.clear_embeds()
        if embeds is not MISSING:
            for embed in embeds:
                m = m.add_embed(embed)
        return m

    def add_embed(self, embed: Embed) -> Message:
        """
        Add an embed to the message.

        Raises:
            ValueError:
                Number of embeds exceeds 10.
        """
        if self.embeds is not MISSING and len(self.embeds) >= 10:
            raise ValueError("Cannot add more than 10 embeds to a message.")
        return replace(
            self,
            embeds=(*self.embeds, embed)
            if self.embeds is not MISSING
            else (embed,),
        )

    def clear_embeds(self) -> Message:
        """
        Clear the embeds of the message.
        """
        return replace(self, embeds=MISSING)

    def set_shared_client_theme(
        self, theme: SharedClientTheme | MISSING = MISSING
    ) -> Message:
        """
        Add a shared client theme to the message.
        """
        return replace(self, shared_client_theme=theme)

    def set_poll(self, poll: Poll | MISSING = MISSING) -> Message:
        """
        Add a poll to the message.
        """
        return replace(self, poll=poll)

    def set_components(
        self,
        components: tuple[Component, ...] | list[Component] | MISSING = MISSING,
    ) -> Message:
        """
        Set the components of the message.

        Raises:
            ValueError:
                - You can only add an ActionRow for now.
                - Number of components exceeds 5.
        """
        m = self.clear_components()
        if components is not MISSING:
            for component in components:
                m = m.add_component(component)
        return m

    def add_component(self, component: Component) -> Message:
        """
        Add a component to the message.

        Raises:
            ValueError:
                - You can only add an ActionRow for now.
                - Number of components exceeds 5.
        """
        if not isinstance(component, ActionRow):
            raise ValueError("You can only add an ActionRow for now.")
        if self.components is not MISSING and len(self.components) >= 5:
            raise ValueError("You can only have 5 components for now.")
        return replace(
            self,
            components=(*self.components, component)
            if self.components is not MISSING
            else (component,),
        )

    def clear_components(self) -> Message:
        """
        Clear all components from the message.
        """
        return replace(self, components=MISSING)

    def set_attachments(
        self,
        attachments: tuple[Attachment, ...]
        | list[Attachment]
        | MISSING = MISSING,
    ) -> Message:
        """
        Set the attachments of the message.
        """
        m = self.clear_attachments()
        if attachments is not MISSING:
            for attachment in attachments:
                m = m.add_attachment(attachment)
        return m

    def add_attachment(self, attachment: Attachment) -> Message:
        """
        Add an attachment to the message.
        """
        return replace(
            self,
            attachments=(*self.attachments, attachment)
            if self.attachments is not MISSING
            else (attachment,),
        )

    def clear_attachments(self) -> Message:
        """
        Clear the attachments of the message.
        """
        return replace(self, attachments=MISSING)

    async def send(self, channel: int | Snowflake | Channel) -> Message:
        """*|coro|*

        Send the message to the specified channel.

        Raises:
            ZcordError:
                - Cannot send a message that already has an ID.
        """
        if self.id is not MISSING:
            raise ZcordError("Cannot send a message that already has an ID")
        assert self._state is not MISSING
        return await self._state.send_message(channel_id=channel, message=self)

    async def reply(self, message: Message) -> Message:
        """*|coro|*

        Reply to the message.

        Raises:
            ZcordError:
                - Cannot reply to a message with no ID.
                - Cannot reply to a message with no channel ID.
        """
        if self.id is MISSING:
            raise ZcordError("Cannot reply to a message with no ID.")
        if self.channel_id is MISSING:
            raise ZcordError("Cannot reply to a message with no channel ID.")
        message = replace(
            message,
            message_reference=MessageReference(message_id=self.id),
        )
        return await message.send(self.channel_id)


@dataclass(frozen=True, slots=True)
class Resolved(Model):
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
