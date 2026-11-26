from enum import IntFlag


class LobbyMemberFlags(IntFlag):
    CAN_LINK_LOBBY = 1 << 0
    """User can link a text channel to a lobby."""
