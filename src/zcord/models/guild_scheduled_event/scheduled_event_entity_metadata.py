from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ScheduledEventEntityMetadata(Model):
    location: str | MISSING = MISSING
    """Location of the event."""


type GuildScheduledEventEntityMetadata = ScheduledEventEntityMetadata
"""An alias for ScheduledEventEntityMetadata."""
