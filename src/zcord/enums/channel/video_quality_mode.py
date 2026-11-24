from enum import IntEnum


class VideoQualityMode(IntEnum):
    AUTO = 1
    """Discord chooses the quality for optimal performance."""

    FULL = 2
    """720p."""
