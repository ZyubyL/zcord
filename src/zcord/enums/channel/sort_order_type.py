from enum import IntEnum


class SortOrderType(IntEnum):
    LATEST_ACTIVITY = 0
    """Sort forum posts by activity."""

    CREATION_DATE = 1
    """Sort forum posts by creation time (from most recent to oldest)."""
