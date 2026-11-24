from enum import IntEnum


class DefaultForumLayoutType(IntEnum):
    NOT_SET = 0
    """No default has been set for forum channel."""

    LIST_VIEW = 1
    """Display posts as a list."""

    GALLERY_VIEW = 2
    """Display posts as a collection of tiles."""
