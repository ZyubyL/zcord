from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivitySecrets(Model):
    """Secrets for Rich Presence joining and spectating."""

    join: str | MISSING = MISSING
    """Secret for joining a party."""

    spectate: str | MISSING = MISSING
    """Secret for spectating a game."""

    match: str | MISSING = MISSING
    """Secret for a specific instanced match."""
