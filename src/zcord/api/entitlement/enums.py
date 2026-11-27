from enum import IntEnum


class EntitlementType(IntEnum):
    PURCHASE = 1
    """Entitlement was purchased by user."""

    PREMIUM_SUBSCRIPTION = 2
    """Entitlement for Discord Nitro subscription."""

    DEVELOPER_GIFT = 3
    """Entitlement was gifted by developer."""

    TEST_MODE_PURCHASE = 4
    """Entitlement was purchased by a dev in application test mode."""

    FREE_PURCHASE = 5
    """Entitlement was granted when the SKU was free."""

    USER_GIFT = 6
    """Entitlement was gifted by another user."""

    PREMIUM_PURCHASE = 7
    """Entitlement was claimed by user for free as a Nitro Subscriber."""

    APPLICATION_SUBSCRIPTION = 8
    """Entitlement was purchased as an app subscription."""
