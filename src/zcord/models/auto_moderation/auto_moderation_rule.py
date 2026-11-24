from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.auto_moderation.auto_moderation_action import (
    AutoModerationAction,
)
from zcord.models.auto_moderation.trigger_metadata import TriggerMetadata
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AutoModerationRule(Model):
    id: Snowflake
    """The ID of this rule."""

    guild_id: Snowflake
    """The ID of the guild this rule belongs to."""

    name: str
    """The rule name."""

    creator_id: Snowflake
    """The user who first created this rule."""

    event_type: enums.EventType
    """The rule event type."""

    trigger_type: enums.TriggerType
    """The rule trigger type."""

    trigger_metadata: TriggerMetadata
    """The rule trigger metadata."""

    actions: tuple[AutoModerationAction, ...]
    """The actions which will execute when the rule is triggered."""

    enabled: bool
    """Whether the rule is enabled."""

    excempt_roles: tuple[Snowflake, ...]
    """The role IDs that should not be affected by the rule."""

    excempt_channels: tuple[Snowflake, ...]
    """The channel IDs that should not be affected by the rule."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "guild_id": Snowflake,
        "creator_id": Snowflake,
        "event_type": enums.EventType,
        "trigger_type": enums.TriggerType,
        "trigger_metadata": TriggerMetadata,
        "actions": AutoModerationAction,
        "excempt_roles": Snowflake,
        "excempt_channels": Snowflake,
    }
