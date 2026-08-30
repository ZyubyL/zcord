from __future__ import annotations

from enum import Enum


class GatewayEvent(Enum):
    """
    Represent the event name sent from the gateway.
    """

    def __str__(self) -> str:
        return self.value

    READY = "READY"
    """
    The bot has successfully connected to the gateway.

    The event contains the bot's [`User`][zcord.User] object.
    """

    GUILD_CREATE = "GUILD_CREATE"
    """
    The bot has joined a guild.

    The event contains the guild's [`Guild`][zcord.Guild] object.
    """

    GUILD_UPDATE = "GUILD_UPDATE"
    """
    The guild has been updated.

    The event contains the old and updated [`Guild`][zcord.Guild] objects.
    """

    MESSAGE_CREATE = "MESSAGE_CREATE"
    """
    A message has been created.

    The event contains the message's [`Message`][zcord.Message] object.
    """
