from __future__ import annotations

from enum import IntFlag


class AttachmentFlags(IntFlag):
    """
    | Flag | Value |
    |------|-------|
    | `NONE` | `0` |
    | `IS_CLIP` | `1 << 0` |
    | `IS_THUMBNAIL` | `1 << 1` |
    | `IS_REMIX` | `1 << 2` |
    | `IS_SPOILER` | `1 << 3` |
    | `IS_ANIMATED` | `1 << 5` |
    """

    NONE = 0
    IS_CLIP = 1 << 0
    IS_THUMBNAIL = 1 << 1
    IS_REMIX = 1 << 2
    IS_SPOILER = 1 << 3
    IS_ANIMATED = 1 << 5
