from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.auto_moderation.action_metadata import ActionMetadata
from zcord.models.base import Model


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
