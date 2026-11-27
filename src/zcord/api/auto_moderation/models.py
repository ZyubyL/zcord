from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class TriggerMetadata(Model):
    keyword_filter: tuple[str, ...]
    """Trigger types: KEYWORD, MEMBER_PROFILE

    Substrings which will be searched for in content."""

    regex_patterns: tuple[str, ...]
    """Trigger types: KEYWORD, MEMBER_PROFILE

    Regular expression patterns which will be matched against content."""

    presets: tuple[enums.KeywordPresetType, ...]
    """Trigger types: KEYWORD_PRESET

    The internally pre-defined wordsets which will be searched for in \
    content."""

    allow_list: tuple[str, ...]
    """Trigger types: KEYWORD, KEYWORD_PRESET, MEMBER_PROFILE

    Substrings which should not trigger the rule."""

    mention_total_limit: int
    """Trigger types: MENTION_SPAM

    Total number of unique role and user mentions allowed per message."""

    mention_raid_protection_enabled: bool
    """Trigger types: MENTION_SPAM

    Whether to automatically detect mention raids."""

    _transforms: ClassVar[dict[str, Any]] = {
        "presets": enums.KeywordPresetType,
    }


@dataclass(frozen=True, slots=True)
class ActionMetadata(Model):
    channel_id: Snowflake
    """Associated action type: SEND_ALERT_MESSAGE

    Channel to which user content should be logged.

    Constraints: existing channel."""

    duration_seconds: int
    """Associated action type: TIMEOUT

    Timeout duration in seconds

    Constraints: maximum of 2419200 seconds (4 weeks)."""

    custom_message: str | None | MISSING = MISSING
    """Associated action type: BLOCK_MESSAGE

    Additional explanation that will be shown to members whenever \
    their message is blocked.

    Constraints: maximum of 150 characters"""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class AutoModerationAction(Model):
    type: enums.ActionType
    """The type of action."""

    metadata: ActionMetadata
    """Additional metadata needed during execution for this specific \
    action type."""

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.ActionType,
        "metadata": ActionMetadata,
    }


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
