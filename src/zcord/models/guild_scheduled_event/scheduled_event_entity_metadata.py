from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class GuildScheduledEventEntityMetadata(Model):
    location: str | MISSING = MISSING
    """Location of the event."""
