from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class InviteMetadata(Model):
    uses: int
    """Number of times this invite has been used."""

    max_uses: int
    """Maximum number of times this invite can be used."""

    max_age: int
    """Duration (in seconds) after which the invite expires."""

    temporary: bool
    """Whether this invite only grants temporary membership."""

    created_at: datetime
    """When this invite was created."""

    _transforms: ClassVar[dict[str, Any]] = {
        "created_at": datetime.fromisoformat,
    }
