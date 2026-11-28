from enum import IntFlag


class SkuFlags(IntFlag):
    AVAILABLE = 1 << 2
    """SKU is available for purchase."""

    GUILD_SUBSCRIPTION = 1 << 7
    """Recurring SKU that can be purchased by a user \
    and applied to a single server. \
    Grants access to every user in that server."""

    USER_SUBSCRIPTION = 1 << 8
    """Recurring SKU purchased by a user for themselves. \
    Grants access to the purchasing user in every server."""
