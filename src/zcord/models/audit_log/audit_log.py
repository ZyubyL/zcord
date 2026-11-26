from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.audit_log.audit_log_entry import AuditLogEntry
from zcord.models.auto_moderation.auto_moderation_rule import (
    AutoModerationRule,
)
from zcord.models.base import Model
from zcord.models.channel.channel import Channel
from zcord.models.guild.integration import Integration
from zcord.models.guild_scheduled_event.scheduled_event import (
    GuildScheduledEvent,
)
from zcord.models.user.user import User


@dataclass(frozen=True, slots=True)
class AuditLog(Model):
    application_commands: tuple[ApplicationCommand, ...]
    """Tuple of application commands referenced in the audit log."""

    audit_log_entries: tuple[AuditLogEntry, ...]
    """Tuple of audit log entries, sorted from most to least recent."""

    auto_moderation_rules: tuple[AutoModerationRule, ...]
    """Tuple of auto moderation rules referenced in the audit log."""

    guild_scheduled_events: tuple[GuildScheduledEvent, ...]
    """Tuple of guild scheduled events referenced in the audit log."""

    integrations: tuple[Integration, ...]
    """Tuple of partial integration objects."""

    threads: tuple[Channel, ...]
    """Tuple of threads referenced in the audit log."""

    users: tuple[User, ...]
    """Tuple of users referenced in the audit log."""

    webhooks: tuple[Webhook, ...]
    """Tuple of webhooks referenced in the audit log."""

    _transforms: ClassVar[dict[str, Any]] = {
        "application_commands": ApplicationCommand,
        "audit_log_entries": AuditLogEntry,
        "auto_moderation_rules": AutoModerationRule,
        "guild_scheduled_events": GuildScheduledEvent,
        "integrations": Integration,
        "threads": Channel,
        "users": User,
        "webhooks": Webhook,
    }
