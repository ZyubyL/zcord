from enum import IntFlag


class GuildInviteFlags(IntFlag):
    IS_GUEST_INVITE = 1 << 0
    """This invite is a guest invite for a voice channel."""
