from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class RoleColors(Model):
    primary_color: int = 0
    """The primary color of the role."""

    secondary_color: int | None = None
    """The secondary color of the role.

    This will make the role a gradient between the other provided colors.
    """

    tertiary_color: int | None = None
    """The tertiary color of the role.

    This will turn the gradient into a holographic style.
    """

    @classmethod
    def from_payload(
        cls, payload: dict[str, Any] | None | MISSING
    ) -> RoleColors | MISSING:
        if payload is MISSING:
            return MISSING
        if payload is None:
            return cls()
        return cls(
            primary_color=payload.get("primary_color", 0),
            secondary_color=payload.get("secondary_color"),
            tertiary_color=payload.get("tertiary_color"),
        )
