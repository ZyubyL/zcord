from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple

from zcord.missing import MISSING
from zcord.models.base import Model


class ActivityPartySize(NamedTuple):
    current_size: int
    max_size: int


@dataclass(frozen=True, slots=True)
class ActivityParty(Model):
    """Contain information for the current party of the player."""

    id: str | MISSING = MISSING
    """The ID of the party."""

    size: ActivityPartySize | MISSING = MISSING
