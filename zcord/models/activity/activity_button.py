from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivityButton(Model):
    """Contain information about the button in the activity card."""

    label: str
    """The button label."""

    url: str | MISSING = MISSING
    """The URL of the button."""
