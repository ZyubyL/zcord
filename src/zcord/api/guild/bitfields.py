from enum import IntFlag


class GuildMemberFlags(IntFlag):
    DEFAULT = 0

    DID_REJOIN = 1 << 0
    """Member has left and rejoin the guild."""

    COMPLETED_ONBOARDING = 1 << 1
    """Member has completed the onboarding process."""

    BYPASSES_VERIFICATION = 1 << 2
    """Member is excempt from guild verification."""

    STARTED_ONBOARDING = 1 << 3
    """Member has started the onboarding process."""

    IS_GUEST = 1 << 4
    """Member is a guest and can only access the invited voice channel."""

    STARTED_HOME_ACTIONS = 1 << 5
    """Member has started the Server Guide new member actions."""

    COMPLETED_HOME_ACTIONS = 1 << 6
    """Member has completed the Server Guide new member actions."""

    AUTOMOD_QUARANTINED_USERNAME = 1 << 7
    """Member has been quarantined by the automod system \
    because of their username, display name or nickname."""

    DM_SETTINGS_UPSELL_ACKNOWLEDGED = 1 << 9
    """Member has dismissed the DM settings upsell."""

    AUTOMOD_QUARANTINED_GUILD_TAG = 1 << 10
    """Member has been quarantined by the automod system \
    because of their guild tag."""


class SystemChannelFlags(IntFlag):
    NONE = 0

    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    """Suppress member join notifications."""

    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    """Suppress server boost notifications."""

    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    """Suppress server setup tips."""

    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    """Hide member join sticker reply buttons."""

    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    """Suppress role subscription purchase and renewal notifications."""

    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5
    """Hide role subscription sticker reply buttons."""
