from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields, enums
from zcord.api.model import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Sku(Model):
    id: Snowflake
    """ID of SKU."""

    type: enums.SkuType
    """Type of SKU."""

    application_id: Snowflake
    """ID of the parent application."""

    name: str
    """Customer-facing name of your premium offering."""

    slug: str
    """System-generated URL slug based on the SKU's name."""

    flags: bitfields.SkuFlags
    """SKU flags combined as a bitfield."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.SkuType,
        "application_id": Snowflake,
        "flags": bitfields.SkuFlags,
    }
