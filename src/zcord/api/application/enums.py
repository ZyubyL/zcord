from enum import IntEnum


class EventWebhookStatus(IntEnum):
    """Status indicating whether event webhooks are enabled or disabled for \
    an application."""

    DISABLED = 1
    """Webhook events are disabled by developer."""

    ENABLED = 2
    """Webhook events are enabled by developer."""

    DISABLED_BY_DISCORD = 3
    """Webhook events are disabled by Discord, usually due to inactivity."""


class ApplicationIntegrationType(IntEnum):
    GUILD_INSTALL = 0
    """App is installable to servers."""

    USER_INSTALL = 1
    """App is installable to users."""
