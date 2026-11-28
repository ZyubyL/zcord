from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Subscription(Model):
    id: Snowflake
    """ID of the subscription."""

    user_id: Snowflake
    """ID of the user who is subscribed."""

    sku_ids: tuple[Snowflake, ...]
    """Tuple of SKUs subscribed to."""

    entitlement_ids: tuple[Snowflake, ...]
    """Tuple of entitlements granted for this subscription."""

    current_period_start: datetime
    """Start of the current subscription period."""

    current_period_end: datetime
    """End of the current subscription period."""

    status: enums.SubscriptionStatus
    """Current status of the subscription."""

    renewal_sku_ids: tuple[Snowflake, ...] | None = None
    """Tuple of SKUs that this user will be subscribed to at renewal."""

    canceled_at: datetime | None = None
    """When the subscription was canceled."""

    country: str | MISSING = MISSING
    """ISO3166-1 alpha-2 country code of the payment source used to purchase \
    the subscription. Missing unless queried with a private OAuth scope."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "user_id": Snowflake,
        "sku_ids": Snowflake,
        "entitlement_ids": Snowflake,
        "renewal_sku_ids": Snowflake,
        "current_period_start": datetime.fromisoformat,
        "current_period_end": datetime.fromisoformat,
        "status": enums.SubscriptionStatus,
        "canceled_at": datetime.fromisoformat,
    }
