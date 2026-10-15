from __future__ import annotations

from enum import StrEnum


class GatewayEvent(StrEnum):
    """Represent the event name sent from the gateway."""

    def __str__(self) -> str:
        return self.value

    READY = "READY"
    """The bot has successfully connected to the gateway.

    This event contains the bot's [`User`][zcord.User] object.
    """

    GUILD_CREATE = "GUILD_CREATE"
    """The bot has joined a guild.

    This event will also fire when the bot first connected to the gateway.

    This event contains the guild's [`Guild`][zcord.Guild] object.
    """

    GUILD_UPDATE = "GUILD_UPDATE"
    """The guild has been updated.

    This event contains the old and updated [`Guild`][zcord.Guild] objects.
    """

    GUILD_DELETE = "GUILD_DELETE"
    """The bot has been removed from the guild, or the guild has been deleted.

    This event contains the deleted [`Guild`][zcord.Guild] object. If it is \
    cached.
    """

    MESSAGE_CREATE = "MESSAGE_CREATE"
    """A message has been created.

    This event contains a [`Message`][zcord.Message] object.
    """

    MESSAGE_UPDATE = "MESSAGE_UPDATE"
    """The message has been updated.

    This event contains the old and an updated [`Message`][zcord.Message] \
    objects.
    """

    MESSAGE_DELETE = "MESSAGE_DELETE"
    """The message has been deleted.

    This event contains the deleted [`Message`][zcord.Message] object. If it \
    is cached.
    """

    MESSAGE_DELETE_BULK = "MESSAGE_DELETE_BULK"
    """Some messages has been deleted.

    This event contains the deleted [`Message`][zcord.Message] objects. \
    If they are cached.
    """

    RESUMED = "RESUMED"
    """The connection to the websocket has been resumed."""

    INTERACTION_CREATE = "INTERACTION_CREATE"
    """Someone triggered an interaction.

    This event contains an [`Interaction`][zcord.Interaction] object.
    """

    CHANNEL_CREATE = "CHANNEL_CREATE"
    """A new channel is created.

    This event contains a [`Channel`][zcord.Channel] object.
    """

    CHANNEL_UPDATE = "CHANNEL_UPDATE"
    """A channel has been updated.

    This event contains the old and an updated \
    [`Channel`][zcord.Channel] objects.
    """

    CHANNEL_DELETE = "CHANNEL_DELETE"
    """A channel has been deleted.

    This event contains the deleted [`Channel`][zcord.Channel] object.
    """
