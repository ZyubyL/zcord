from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class Ban(Model):
    reason: str | None
    """The reason for the ban."""

    user: User
    """The banned user."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user": User,
    }
