from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model


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
