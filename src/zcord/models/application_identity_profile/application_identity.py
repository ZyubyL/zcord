from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ApplicationIdentity(Model):
    user_id: Snowflake
    """The Discord user's ID."""

    provider_type: str
    """The external account provider type."""

    provider_issued_user_id: str
    """The user's ID in the external systemm."""

    provider_id: str | MISSING = MISSING
    """Provider-specific identifier used to disambiguate identities."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user_id": Snowflake,
    }
