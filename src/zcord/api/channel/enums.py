from enum import IntEnum


class ChannelType(IntEnum):
    GUILD_TEXT = 0
    """A text channel within a server."""

    DM = 1
    """A direct message between users."""

    GUILD_VOICE = 2
    """A voice channel within a server."""

    GROUP_DM = 3
    """A direct message between multiple users."""

    GUILD_CATEGORY = 4
    """An organizational category that contains up to 50 channels."""

    GUILD_ANNOUNCEMENT = 5
    """A channel that users can follow and crosspost into their own server."""

    ANNOUNCEMENT_THREAD = 10
    """A temporary sub-channel within a GUILD_ANNOUNCEMENT channel."""

    PUBLIC_THREAD = 11
    """A temporary sub-channel within a GUILD_TEXT or GUILD_FORUM channel."""

    PRIVATE_THREAD = 12
    """A temporary sub-channel within a GUILD_TEXT channel \
    that is only viewable by those invited \
    and those with the MANAGE_THREADS permission."""

    GUILD_STAGE_VOICE = 13
    """A voice channel for hosting events with an audience."""

    GUILD_DIRECTORY = 14
    """The channel in a hub containing the listed servers."""

    GUILD_FORUM = 15
    """channel that can only contain threads."""

    GUILD_MEDIA = 16
    """channel that can only contain threads, \
    similar to GUILD_FORUM channels."""


class ForumLayoutType(IntEnum):
    NOT_SET = 0
    """No default has been set for forum channel."""

    LIST_VIEW = 1
    """Display posts as a list."""

    GALLERY_VIEW = 2
    """Display posts as a collection of tiles."""


class OverwriteType(IntEnum):
    ROLE = 0
    MEMBER = 1


class SortOrderType(IntEnum):
    LATEST_ACTIVITY = 0
    """Sort forum posts by activity."""

    CREATION_DATE = 1
    """Sort forum posts by creation time (from most recent to oldest)."""


class VideoQualityMode(IntEnum):
    AUTO = 1
    """Discord chooses the quality for optimal performance."""

    FULL = 2
    """720p."""
