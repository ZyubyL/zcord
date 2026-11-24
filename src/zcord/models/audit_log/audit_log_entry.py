from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.audit_log.audit_log_change import AuditLogChange
from zcord.models.audit_log.optional_audit_entry_info import (
    OptionalAuditEntryInfo,
)
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AuditLogEntry(Model):
    changes: tuple[AuditLogChange, ...]
    """Changes made to the `target_id`."""

    id: Snowflake
    """ID of the entry."""

    action_type: enums.AuditLogEvent
    """Type of action that occurred."""

    target_id: str | None = None
    """ID of the affected entity."""

    user_id: Snowflake | None = None
    """User of app that made the changes."""

    options: OptionalAuditEntryInfo | MISSING = MISSING
    """Additional info for certain event types."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "changes": AuditLogChange,
        "action_type": enums.AuditLogEvent,
        "user_id": Snowflake,
        "options": OptionalAuditEntryInfo,
    }
