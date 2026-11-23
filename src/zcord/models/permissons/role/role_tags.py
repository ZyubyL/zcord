from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


def _null_flag(value: Any) -> bool | MISSING:
    # Discord is very funny on this one and treat null as true
    if value is None:
        return True
    if value is MISSING:
        return MISSING
    return bool(value)


@dataclass(frozen=True, slots=True)
class RoleTags(Model):
    bot_id: Snowflake | MISSING = MISSING
    """The ID of the bot this role belongs to."""

    integration_id: Snowflake | MISSING = MISSING
    """The ID of the integration this role belongs to."""

    premium_subscriber: bool | MISSING = MISSING
    """Whether this the guild's Booster role."""

    subscription_listing_id: Snowflake | MISSING = MISSING
    """The ID of this role's subscription SKU and listing."""

    available_for_purchase: bool | MISSING = MISSING
    """Whether this role is available for purchase."""

    guild_connections: bool | MISSING = MISSING
    """Whether this role is a guild's linked role."""

    _transforms: ClassVar[dict[str, Any]] = {
        "bot_id": Snowflake,
        "integration_id": Snowflake,
        "subscription_listing_id": Snowflake,
        "premium_subscriber": _null_flag,
        "available_for_purchase": _null_flag,
        "guild_connections": _null_flag,
    }
