from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import bitfields, enums
from zcord.api.application.models import Application
from zcord.api.channel.models import Channel
from zcord.api.message.models import MessageActivity
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class SDKDMMessage(Model):
    """Represent a message between provisional users \
    that exists only in-game."""

    id: Snowflake
    """ID of the message."""

    type: enums.MessageType
    """Type of message."""

    content: str
    """Contents of the message."""

    author: User
    """Author of the message."""

    flags: bitfields.MessageFlags
    """Message flags combined as a bitfield."""

    application_id: Snowflake
    """ID of the application that created the message."""

    channel: Channel
    """Channel object with recipient information."""

    activity: MessageActivity | MISSING = MISSING
    """Sent with Rich Presence-related chat embeds."""

    application: Application | MISSING = MISSING
    """Sent with Rich Presence-related chat embeds."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.MessageType,
        "author": User,
        "flags": bitfields.MessageFlags,
        "application_id": Snowflake,
        "channel": Channel,
        "activity": MessageActivity,
        "application": Application,
    }


@dataclass(frozen=True, slots=True)
class LobbyMessage(Model):
    """Represents a message sent in a lobby or Linked Channel."""

    id: Snowflake
    """ID of the message."""

    type: enums.MessageType
    """Type of message."""

    content: str
    """Contents of the message."""

    lobby_id: Snowflake
    """ID of the lobby where the message was sent."""

    channel_id: Snowflake
    """ID of the channel the message was sent in."""

    author: User
    """Author of the message."""

    flags: bitfields.MessageFlags
    """Message flags combined as a bitfield."""

    metadata: dict | MISSING = MISSING
    """Additional metadata for the message (key-value pairs)."""

    application_id: Snowflake | MISSING = MISSING
    """ID of the application."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.MessageType,
        "lobby_id": Snowflake,
        "channel_id": Snowflake,
        "author": User,
        "flags": bitfields.MessageFlags,
        "application_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class EventBody(Model):
    """The event body contains high-level data about the event, \
    like the type and time it was triggered."""

    type: enums.EventBodyType
    """Event type."""

    timestamp: datetime
    """Timestamp of when the event occurred."""

    data: dict
    """Data for the event."""

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.EventBodyType,
        "timestamp": datetime.fromisoformat,
    }


@dataclass(frozen=True, slots=True)
class Payload(Model):
    """The outer webhook payload"""

    version: int
    """Version scheme for the webhook event. Currently always `1`"""

    application_id: Snowflake
    """ID of your app."""

    type: enums.WebhookEventType
    """Type of webhook."""

    event: EventBody | MISSING = MISSING
    """Event data payload."""

    _transforms: ClassVar[dict[str, Any]] = {
        "application_id": Snowflake,
        "type": enums.WebhookEventType,
        "event": EventBody,
    }
