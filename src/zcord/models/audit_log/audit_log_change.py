from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class AuditLogChange(Model):
    # TODO: Exception https://docs.discord.com/developers/resources/audit-log#audit-log-change-object-audit-log-change-exceptions

    key: str
    """Name of the changed entity, with a few exceptions."""

    new_value: Any | MISSING = MISSING
    """New value of the key."""

    old_value: Any | MISSING = MISSING
    """Old value of the key."""
