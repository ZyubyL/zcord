from enum import IntEnum


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    """Members will receive notifications for all messages by default."""

    ONLY_MENTIONS = 1
    """Members will receive notifications only for messages that @mention them \
    by default."""
