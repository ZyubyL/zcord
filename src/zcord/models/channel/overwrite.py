from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Overwrite(Model):
    id: Snowflake
    """Role or user ID."""

    type: enums.OverwriteType
    """Ovewrite type."""

    allow: str
    """Allowed permissions."""

    deny: str
    """Denied permissions."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.OverwriteType,
    }
