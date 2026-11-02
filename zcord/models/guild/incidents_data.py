from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class IncidentsData(Model):
    """The incidents data for the Guild."""

    invites_disabled_until: datetime | None
    """When invites get enabled again"""

    dms_disabled_until: datetime | None
    """When direct messages get enabled again"""

    dm_spam_detected_at: datetime | None | MISSING = MISSING
    """When the DM spam was detected"""

    raid_detected_at: datetime | None | MISSING = MISSING
    """When the raid was detected"""

    _transforms: ClassVar[dict] = {
        "invites_disabled_until": datetime.fromisoformat,
        "dms_disabled_until": datetime.fromisoformat,
        "dm_spam_detected_at": datetime.fromisoformat,
        "raid_detected_at": datetime.fromisoformat,
    }
