from __future__ import annotations

from enum import IntEnum


class MessageNotificationLevel(IntEnum):
    """
    The default message notification level of the guild.

    | Level | Value | Description |
    |-------|-------|-------------|
    | `ALL_MESSAGES` | `0` | Members will receive \
    notifications for all messages. |
    | `ONLY_MENTIONS` | `1` | Members will only receive notifications for \
    messages that mentions them. |
    """

    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1
