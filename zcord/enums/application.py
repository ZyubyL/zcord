from __future__ import annotations

from enum import IntEnum


class EventWebhookStatus(IntEnum):
    """
    Status indicating whether event webhooks are enabled or disabled for an \
    application.

    | Name | Value |
    |------|-------|
    | `DISABLED` | `1` |
    | `ENABLED` | `2` |
    | `DISABLED_BY_DISCORD` | `3` |
    """
