from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Entitlement(Model):
    id: Snowflake
    """ID of the entitlement."""

    sku_id: Snowflake
    """ID of the SKU."""

    application_id: Snowflake
    """ID of the parent application."""

    type: enums.EntitlementType
    """Type of entitlement."""

    deleted: bool
    """Entitlement was deleted."""

    user_id: Snowflake | MISSING = MISSING
    """ID of the user that is granted access to the entitlement's SKU."""

    starts_at: datetime | None = None
    """Start date at which the entitlement is valid."""

    ends_at: datetime | None = None
    """Date at which the entitlement is no longer valid."""

    guild_id: Snowflake | MISSING = MISSING
    """ID of the guild that is granted access to the entitlement's SKU."""

    consumed: bool | MISSING = MISSING
    """For consumable items, \
    whether or not the entitlement has been consumed."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "sku_id": Snowflake,
        "application_id": Snowflake,
        "type": enums.EntitlementType,
        "user_id": Snowflake,
        "starts_at": datetime.fromisoformat,
        "ends_at": datetime.fromisoformat,
        "guild_id": Snowflake,
    }
