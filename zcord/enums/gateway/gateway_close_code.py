from __future__ import annotations

from enum import IntEnum


class GatewayCloseCode(IntEnum):
    UNKNOWN_ERROR = 4000

    UNKNOWN_OPCODE = 4001
    """
    Discord received an invalid GatewayOpcode.
    """

    DECODE_ERROR = 4002
    """
    Discord received an invalid payload.
    """

    NOT_AUTHENTICATED = 4003
    """
    The session has not been authenticated.
    """

    AUTHENTICATION_FAILED = 4004
    """
    Invalid authentication token.
    """

    ALREADY_AUTHENTICATED = 4005
    """
    More than one identity payload were sent.
    """

    INVALID_SEQUENCE = 4007
    """
    Invalid resuming sequence.
    """

    RATE_LIMITED = 4008
    """
    You have been rate limited.
    """

    SESSION_TIMED_OUT = 4009
    """
    Timed out session.
    """

    INVALID_SHARDS = 4010
    """
    Invalid shard in identity payload.
    """

    SHARDING_REQUIRED = 4011
    """
    You are required to shard the connection.
    """

    INVALID_API_VERSION = 4012
    """
    You sent an invalid API version.
    """

    INVALID_INTENTS = 4013
    """
    Invalid intents were sent.
    """

    DISALLOWED_INTENTS = 4014
    """
    Not enabled or disallowed priviledge intents were sent.
    """
