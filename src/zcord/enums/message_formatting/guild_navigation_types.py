from enum import StrEnum


class GuildNavigationTypes(StrEnum):
    """The corresponding resource in the current server."""

    CHANNEL_AND_ROLE = "customize"
    BROWSE_CHANNELS = "browse"
    SERVER_GUIDE = "guide"
    LINKED_ROLES = "linked-roles"
