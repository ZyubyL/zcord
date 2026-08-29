from __future__ import annotations

from enum import Enum


class GatewayEvent(Enum):
    """
    Represent the event name sent from the gateway.
    """

    def __str__(self) -> str:
        return self.value

    READY = "READY"
    GUILD_CREATE = "GUILD_CREATE"
    GUILD_UPDATE = "GUILD_UPDATE"
    MESSAGE_CREATE = "MESSAGE_CREATE"
