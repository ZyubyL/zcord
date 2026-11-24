from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.application_identity_profile.profile_data import ProfileData
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ApplicationIdentityProfile(Model):
    username: str | None = None
    """The user's username in the external system."""

    metadata: Any | None = None
    """Arbitrary game-defined data."""

    data: ProfileData | None = None
    """The profile data containing game stats."""

    _transforms: ClassVar[dict[str, Any]] = {
        "data": ProfileData,
    }
