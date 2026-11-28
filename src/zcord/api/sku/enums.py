from enum import IntEnum


class SkuType(IntEnum):
    DURABLE = 2
    """Durable one-time purchase."""

    CONSUMABLE = 3
    """Consumable one-time purchase."""

    SUBSCRIPTION = 5
    """Represents a recurring subscription."""

    SUBSCRIPTION_GROUP = 6
    """System-generated group for each SUBSCRIPTION SKU created."""
