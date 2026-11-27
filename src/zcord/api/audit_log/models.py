from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.auto_moderation.models import AutoModerationRule
from zcord.api.channel.models import Channel
from zcord.api.guild.models import Integration
from zcord.api.guild_scheduled_event.models import GuildScheduledEvent
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AuditLogChange(Model):
    # TODO: Exception https://docs.discord.com/developers/resources/audit-log#audit-log-change-object-audit-log-change-exceptions

    key: str
    """Name of the changed entity, with a few exceptions."""

    new_value: Any | MISSING = MISSING
    """New value of the key."""

    old_value: Any | MISSING = MISSING
    """Old value of the key."""


@dataclass(frozen=True, slots=True)
class OptionalAuditEntryInfo(Model):
    application_id: Snowflake
    """ID of the app whose permissions were targeted.

    Event types: APPLICATION_COMMAND_PERMISSION_UPDATE."""

    auto_moderation_rule_name: str
    """Name of the Auto Moderation rule that was triggered.

    Event types: AUTO_MODERATION_BLOCK_MESSAGE &
    AUTO_MODERATION_FLAG_TO_CHANNEL &
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED &
    AUTO_MODERATION_QUARANTINE_USER."""

    auto_moderation_rule_trigger_type: str
    """Trigger type of the Auto Moderation rule that was triggered.

    Event types: AUTO_MODERATION_BLOCK_MESSAGE &
    AUTO_MODERATION_FLAG_TO_CHANNEL &
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED &
    AUTO_MODERATION_QUARANTINE_USER."""

    channel_id: Snowflake
    """Channel in which the entities were targeted.

    Event types: MEMBER_MOVE & MESSAGE_PIN & MESSAGE_UNPIN & MESSAGE_DELETE &
    STAGE_INSTANCE_CREATE & STAGE_INSTANCE_UPDATE & STAGE_INSTANCE_DELETE &
    AUTO_MODERATION_BLOCK_MESSAGE & AUTO_MODERATION_FLAG_TO_CHANNEL &
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED &
    AUTO_MODERATION_QUARANTINE_USER & VOICE_CHANNEL_STATUS_CREATE &
    VOICE_CHANNEL_STATUS_DELETE."""

    count: str
    """Number of entities that were targeted, or number of position updates.

    Event types: MESSAGE_DELETE & MESSAGE_BULK_DELETE & MEMBER_DISCONNECT &
    MEMBER_MOVE & CHANNEL_POSITION_UPDATE & ROLE_POSITION_UPDATE."""

    delete_member_days: str
    """Number of days after which inactive members were kicked.

    Event types: MEMBER_PRUNE"""

    id: Snowflake
    """ID of the overwritten entity
    Event types: CHANNEL_OVERWRITE_CREATE & CHANNEL_OVERWRITE_UPDATE &
    CHANNEL_OVERWRITE_DELETE"""

    members_removed: str
    """Number of members removed by the prune
    Event types: MEMBER_PRUNE"""

    message_id: Snowflake
    """ID of the message that was targeted
    Event types: MESSAGE_PIN & MESSAGE_UNPIN"""

    role_name: str
    """Name of the role if type is "0" (not present if type is "1")
    Event types: CHANNEL_OVERWRITE_CREATE &
    CHANNEL_OVERWRITE_UPDATE & CHANNEL_OVERWRITE_DELETE"""

    type: str
    """Type of overwritten entity - role ("0") or member ("1")
    Event types: CHANNEL_OVERWRITE_CREATE &
    CHANNEL_OVERWRITE_UPDATE & CHANNEL_OVERWRITE_DELETE"""

    integration_type: str
    """The type of integration which performed the action
    Event types: MEMBER_KICK & MEMBER_ROLE_UPDATE"""

    status: str
    """The new voice channel status
    Event types: VOICE_CHANNEL_STATUS_CREATE"""

    _transforms: ClassVar[dict[str, Any]] = {
        "application_id": Snowflake,
        "channel_id": Snowflake,
        "id": Snowflake,
        "message_id": Snowflake,
    }


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
