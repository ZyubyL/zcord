from enum import IntEnum


class SubscriptionStatus(IntEnum):
    ACTIVE = 0
    """Subscription is active and scheduled to renew."""

    INACTIVE = 1
    """Subscription is inactive and not being charged."""

    ENDING = 2
    """Subscription is active but will not renew."""
