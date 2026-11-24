from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.application_identity_profile.dynamic_field import DynamicField
from zcord.models.application_identity_profile.primary_profile_data import (
    PrimaryProfileData,
)
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ProfileData(Model):
    primary: PrimaryProfileData | MISSING = MISSING
    """Pre-configured game stat fields."""

    dynamic: tuple[DynamicField, ...] | MISSING = MISSING
    """Custom game stat fields."""

    _transforms: ClassVar[dict[str, Any]] = {
        "primary": PrimaryProfileData,
        "dynamic": DynamicField,
    }
