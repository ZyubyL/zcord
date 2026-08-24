from __future__ import annotations

from enum import IntFlag


class ChannelFlags(IntFlag):
    """
    | Flag | Value |
    |------|-------|
    | `NONE` | `0` |
    | `PINNED` | `1 << 1` |
    | `REQUIRE_TAG` | `1 << 4` |
    | `HIDE_MEDIA_DOWNLOAD_OPTIONS` | `1 << 15` |
    | `IS_SPOILER_CHANNEL` | `1 << 21` |
    """

    NONE = 0
    PINNED = 1 << 1
    REQUIRE_TAG = 1 << 4
    HIDE_MEDIA_DOWNLOAD_OPTIONS = 1 << 15
    IS_SPOILER_CHANNEL = 1 << 21
