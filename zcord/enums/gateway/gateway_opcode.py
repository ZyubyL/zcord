from __future__ import annotations

from enum import IntEnum


class GatewayOpcode(IntEnum):
    HELLO = 10
    HEARTBEAT = 1
    HEARTBEAT_ACK = 11
    IDENTIFY = 2
    DISPATCH = 0
    RESUME = 6
    RECONNECT = 7
    INVALID_SESSION = 9
