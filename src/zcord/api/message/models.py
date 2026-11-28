from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar, Self

from zcord import bitfields, enums
from zcord.api.application.models import Application
from zcord.api.channel.models import Channel
from zcord.api.emoji.models import Emoji
from zcord.api.model import Model
from zcord.api.poll.models import Poll
from zcord.api.sticker.models import StickerItem
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class SharedClientTheme(Model):
    colors: tuple[str, ...]
    """The hexadecimal-encoded colors of the theme (max of 5)."""

    gradient_angle: int
    """The direction of the theme's colors (max of 360)."""

    base_mix: int
    """The intensity of the theme's colors (max of 100)."""

    base_theme: enums.BaseTheme | None | MISSING = MISSING
    """The mode of the theme."""

    _transforms: ClassVar[dict[str, Any]] = {
        "base_theme": enums.BaseTheme,
    }


@dataclass(frozen=True, slots=True)
class MessagePin(Model):
    pinned_at: datetime
    """The time the message was pinned."""

    message: Message
    """The pinned message."""

    _transforms: ClassVar[dict[str, Any]] = {
        "pinned_at": datetime.fromisoformat,
    }


@dataclass(frozen=True, slots=True)
class RoleSubscriptionData(Model):
    role_subscription_listing_id: Snowflake
    """The ID of the sku and listing that the user is subscribed to."""

    tier_name: str
    """The name of the tier that the user is subscribed to."""

    total_months_subscribed: int
    """The cumulative number of months that the user has been subscribed for."""

    is_renewal: bool
    """Whether this notification is for a renewal rather than a new purchase."""

    _transforms: ClassVar[dict[str, Any]] = {
        "role_subscription_listing_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class ChannelMention(Model):
    id: Snowflake
    """ID of the channel."""

    guild_id: Snowflake
    """ID of the guild containing the channel."""

    type: int
    """The type of channel."""

    name: str
    """The name of the channel."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "guild_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class Attachment(Model):
    id: Snowflake
    """Attachment ID."""

    filename: str
    """Name of file attached."""

    size: int
    """Size of file in bytes."""

    url: str
    """Source url of file."""

    proxy_url: str
    """A proxied url of file."""

    title: str | MISSING = MISSING
    """The title of the file."""

    description: str | MISSING = MISSING
    """Description (alt text) for the file."""

    content_type: str | MISSING = MISSING
    """The attachment's media type."""

    height: int | None | MISSING = MISSING
    """Height of file (if image or video)."""

    width: int | None | MISSING = MISSING
    """Width of file (if image or video)."""

    placeholder: str | MISSING = MISSING
    """Thumbhash placeholder (if image or video)."""

    placeholder_version: int | MISSING = MISSING
    """Version of the placeholder (if image or video)."""

    ephemeral: bool | MISSING = MISSING
    """Whether this attachment is ephemeral."""

    duration_secs: float | MISSING = MISSING
    """The duration of the audio or video file."""

    waveform: str | MISSING = MISSING
    """Base64 encoded bytearray representing a sampled waveform \
    (currently for voice messages)."""

    flags: bitfields.AttachmentFlags | MISSING = MISSING
    """Attachment flags combined as a bitfield."""

    clip_participants: tuple[User, ...] | MISSING = MISSING
    """For Clips, array of users who were in the stream."""

    clip_created_at: datetime | MISSING = MISSING
    """For Clips, when the clip was created."""

    application: Application | None | MISSING = MISSING
    """For Clips, the application in the stream, if recognized."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "flags": bitfields.AttachmentFlags,
        "clip_participants": User,
        "clip_created_at": datetime.fromisoformat,
        "application": Application,
    }


# NOTE: https://docs.discord.com/developers/resources/message#embed-fields-by-embed-type
@dataclass(frozen=True, slots=True)
class EmbedField(Model):
    name: str
    """Name of the field."""

    value: str
    """Value of the field."""

    inline: bool | MISSING = MISSING
    """Whether or not this field should display inline."""


@dataclass(frozen=True, slots=True)
class EmbedFooter(Model):
    text: str
    """Footer text."""

    icon_url: str | MISSING = MISSING
    """URL of footer icon (only supports http(s) and attachments)."""

    proxy_icon_url: str | MISSING = MISSING
    """A proxied url of footer icon."""


@dataclass(frozen=True, slots=True)
class EmbedAuthor(Model):
    name: str
    """Name of author."""

    url: str | MISSING = MISSING
    """URL of author (only supports http(s))."""

    icon_url: str | MISSING = MISSING
    """URL of author icon (only supports http(s) and attachments)."""

    proxy_icon_url: str | MISSING = MISSING
    """A proxied url of author icon."""


@dataclass(frozen=True, slots=True)
class EmbedProvider(Model):
    name: str | MISSING = MISSING
    """Name of provider."""

    url: str | MISSING = MISSING
    """URL of provider."""


@dataclass(frozen=True, slots=True)
class EmbedImage(Model):
    url: str
    """Source URL of image (only supports http(s) and attachments)."""

    proxy_url: str | MISSING = MISSING
    """A proxied URL of the image."""

    height: int | MISSING = MISSING
    """Height of image."""

    width: int | MISSING = MISSING
    """Width of image."""

    content_type: str | MISSING = MISSING
    """The image's media type."""

    placeholder: str | MISSING = MISSING
    """Thumbhash placeholder of the image."""

    placeholder_version: int | MISSING = MISSING
    """Version of the placeholder."""

    description: str | MISSING = MISSING
    """Description (alt text) for the image."""

    flags: bitfields.EmbedFlags | MISSING = MISSING
    """Embed media flags combined as a bitfield."""

    _transforms: ClassVar[dict[str, Any]] = {
        "flags": bitfields.EmbedFlags,
    }


@dataclass(frozen=True, slots=True)
class EmbedAudio(Model):
    url: str | MISSING = MISSING
    """Source URL of audio."""

    proxy_url: str | MISSING = MISSING
    """A proxied URL of the audio."""

    content_type: str | MISSING = MISSING
    """The audio's media type."""

    description: str | MISSING = MISSING
    """Description of the audio"""


@dataclass(frozen=True, slots=True)
class EmbedVideo(Model):
    url: str | MISSING = MISSING
    """Source URL of video."""

    proxy_url: str | MISSING = MISSING
    """A proxied URL of the video."""

    height: int | MISSING = MISSING
    """Height of video."""

    width: int | MISSING = MISSING
    """Width of video."""

    content_type: str | MISSING = MISSING
    """The video's media type."""

    placeholder: str | MISSING = MISSING
    """Thumbhash placeholder of the video."""

    placeholder_version: int | MISSING = MISSING
    """Version of the placeholder."""

    description: str | MISSING = MISSING
    """Description (alt text) for the video."""

    flags: int | MISSING = MISSING
    """Embed media flags combined as a bitfield."""


@dataclass(frozen=True, slots=True)
class Embed(Model):
    title: str | MISSING = MISSING
    """Title of embed."""

    type: enums.EmbedType | MISSING = MISSING
    """Type of embed.

    Notes:
        This is always `"rich"` for webhook events.
    """

    description: str | MISSING = MISSING
    """Description of embed."""

    url: str | MISSING = MISSING
    """URL of embed."""

    timestamp: datetime | MISSING = MISSING
    """Timestamp of embed content."""

    color: int | MISSING = MISSING
    """Color code of the embed."""

    footer: EmbedFooter | MISSING = MISSING
    """Footer information."""

    image: EmbedImage | MISSING = MISSING
    """Image information."""

    thumbnail: EmbedImage | MISSING = MISSING
    """Thumbnail information."""

    video: EmbedVideo | MISSING = MISSING
    """Video information."""

    audio: EmbedAudio | MISSING = MISSING
    """Audio information."""

    provider: EmbedProvider | MISSING = MISSING
    """Provider information."""

    author: EmbedAuthor | MISSING = MISSING
    """Author information."""

    fields: tuple[EmbedField, ...] | MISSING = MISSING
    """Field information."""

    components: tuple[Component, ...] | MISSING = MISSING
    """Components that make up the embed.
    Only present on `components` type embed."""

    flags: bitfields.EmbedFlags | MISSING = MISSING
    """Embed flags combined as a bitfield."""

    _transforms: ClassVar[dict[str, Any]] = {
        "timestamp": datetime.fromisoformat,
        "footer": EmbedFooter,
        "image": EmbedImage,
        "thumbnail": EmbedImage,
        "video": EmbedVideo,
        "audio": EmbedAudio,
        "provider": EmbedProvider,
        "author": EmbedAuthor,
        "fields": EmbedField,
        "components": Component,
        "flags": bitfields.EmbedFlags,
    }


@dataclass(frozen=True, slots=True)
class ReactionCountDetails(Model):
    burst: int
    """Count of super reactions."""

    normal: int
    """Count of normal reactions."""


@dataclass(frozen=True, slots=True)
class Reaction(Model):
    count: int
    """Total number of times this emoji has been used to react \
    (including super reacts)."""

    count_details: ReactionCountDetails
    """Reaction count details object."""

    me: bool
    """Whether the current user reacted using this emoji."""

    me_burst: bool
    """Whether the current user super-reacted using this emoji."""

    emoji: Emoji
    """Emoji information."""

    burst_colors: tuple[int, ...]
    """HEX colors used for super reaction."""

    _transforms: ClassVar[dict[str, Any]] = {
        "count_details": ReactionCountDetails,
        "emoji": Emoji,
    }


@dataclass(frozen=True, slots=True)
class MessageSnapshot(Model):
    message: Message


@dataclass(frozen=True, slots=True)
class MessageReference(Model):
    type: enums.MessageReferenceType | MISSING = MISSING
    """Type of reference."""

    message_id: Snowflake | MISSING = MISSING
    """ID of the originating message."""

    channel_id: Snowflake | MISSING = MISSING
    """ID of the originating message's channel."""

    guild_id: Snowflake | MISSING = MISSING
    """ID of the originating message's guild."""

    fail_if_not_exists: bool | MISSING = MISSING
    """When sending, whether to error if the referenced message doesn't exist \
    instead of sending as a normal (non-reply) message."""

    _transforms: ClassVar[dict[str, Any]] = {
        "message_id": Snowflake,
        "channel_id": Snowflake,
        "guild_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class MessageCall(Model):
    participants: tuple[Snowflake, ...]
    """Tuple of user IDs that participated in the call."""

    ended_timestamp: datetime | None | MISSING = MISSING
    """Time when call ended."""

    _transforms: ClassVar[dict[str, Any]] = {
        "participants": Snowflake,
        "ended_timestamp": datetime.fromisoformat,
    }


@dataclass(frozen=True, slots=True)
class MessageInteractionMetadata(Model):
    id: Snowflake
    """ID of the interaction."""

    type: enums.InteractionType
    """Type of interaction."""

    user: User
    """User who triggered the interaction."""

    authorizing_integration_owners: dict[enums.ApplicationIntegrationType, Any]
    """IDs for installation context(s) related to an interaction."""

    original_response_message_id: Snowflake | MISSING = MISSING
    """ID of the original response message, \
    present only on follow-up messages."""

    target_user: User | MISSING = MISSING
    """The user the command was run on, \
    present only on user command interactions."""

    target_message_id: Snowflake | MISSING = MISSING
    """The ID of the message the command was run on, \
    present only on message command interactions."""

    interacted_message_id: Snowflake | MISSING = MISSING
    """ID of the message that contained the interactive component."""

    triggering_interaction_metadata: Self | MISSING = MISSING
    """Metadata for the interaction that was used to open the modal."""


@dataclass(frozen=True, slots=True)
class MessageActivity(Model):
    type: enums.MessageActivityType
    """Type of message activity."""

    party_id: str | MISSING = MISSING
    """Party ID from a RPC event."""

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.MessageActivityType,
    }


@dataclass(frozen=True, slots=True)
class Message(Model):
    id: Snowflake
    """ID of the message."""

    channel_id: Snowflake
    """ID of the channel the message was sent in."""

    author: User
    """The author of this message."""

    content: str
    """Contents of the message."""

    timestamp: datetime
    """When this message was sent."""

    tts: bool
    """Whether this was a TTS message."""

    mention_everyone: bool
    """Whether this message mentions everyone."""

    mentions: tuple[User, ...]
    """Users specifically mentioned in the message."""

    mention_roles: tuple[Snowflake, ...]
    """Roles specifically mentioned in this message."""

    attachments: tuple[Attachment, ...]
    """Any attached files that are not referenced in embeds or components."""

    embeds: tuple[Embed, ...]
    """Any embedded content."""

    type: enums.MessageType
    """Type of message."""

    pinned: bool
    """Whether this message is pinned."""

    edited_timestamp: datetime | None = None
    """When this message was edited."""

    mention_channels: tuple[ChannelMention, ...] | MISSING = MISSING
    """Channels specifically mentioned in this message."""

    reactions: tuple[Reaction, ...] | MISSING = MISSING
    """Reactions to the message."""

    nonce: int | str | MISSING = MISSING
    """Used to validating a message was sent."""

    webhook_id: Snowflake | MISSING = MISSING
    """If the message is generated by a webhook, this is the webhook's ID."""

    activity: MessageActivity | MISSING = MISSING
    """RPC-related chat embeds."""

    application: Application | MISSING = MISSING
    """RPC-related chat embeds."""

    application_id: Snowflake | MISSING = MISSING
    """If the message is an Interaction or application-owned webhook, \
    this is the ID of the application."""

    flags: bitfields.MessageFlags | MISSING = MISSING
    """Message flags combined as a bitfield."""

    message_reference: MessageReference | MISSING = MISSING
    """Data showing the source of a crosspost, channel follow add, \
    pin, or reply message."""

    message_snapshots: tuple[MessageSnapshot, ...] | MISSING = MISSING
    """The message associated with the `message_reference`."""

    referenced_message: Message | None | MISSING = MISSING
    """The message associated with the `message_reference`."""

    interaction_metadata: MessageInteractionMetadata | MISSING = MISSING
    """Interaction metadata of the message."""

    thread: Channel | MISSING = MISSING
    """The thread that was started from this message."""

    components: tuple[MessageComponent, ...] | MISSING = MISSING
    """Components inside the message."""

    sticker_items: tuple[StickerItem, ...] | MISSING = MISSING
    """Stickers in the message."""

    position: int | MISSING = MISSING
    """A generally increasing integer (there may be gaps or duplicates)\
    that represents the approximate position of the message in a thread."""

    role_subscription_data: RoleSubscriptionData | MISSING = MISSING
    """Data of the role subscription purchase or renewal that prompted this
    `ROLE_SUBSCRIPTION_PURCHASE` message."""

    resolved: Resolved | MISSING = MISSING
    """Data for users, members, channels, and roles referenced \
    in this message."""

    poll: Poll | MISSING = MISSING
    """A poll."""

    call: MessageCall | MISSING = MISSING
    """The call associated with the message."""

    shared_client_theme: SharedClientTheme | MISSING = MISSING
    """The custom client-side theme shared via the message."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "channel_id": Snowflake,
        "author": User,
        "timestamp": datetime.fromisoformat,
        "mentions": User,
        "mention_roles": Snowflake,
        "attachments": Attachment,
        "embeds": Embed,
        "type": enums.MessageType,
        "edited_timestamp": datetime.fromisoformat,
        "mention_channels": ChannelMention,
        "reactions": Reaction,
        "webhook_id": Snowflake,
        "activity": MessageActivity,
        "application": Application,
        "application_id": Snowflake,
        "flags": bitfields.MessageFlags,
        "message_reference": MessageReference,
        "message_snapshots": MessageSnapshot,
        "interaction_metadata": MessageInteractionMetadata,
        "thread": Channel,
        "components": MessageComponent,
        "sticker_items": StickerItem,
        "role_subscription_data": RoleSubscriptionData,
        "resolved": Resolved,
        "poll": Poll,
        "call": MessageCall,
        "shared_client_theme": SharedClientTheme,
    }


Message._transforms["referenced_message"] = Message
MessagePin._transforms["message"] = Message
MessageSnapshot._transforms["message"] = Message
