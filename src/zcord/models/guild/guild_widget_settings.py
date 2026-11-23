from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildWidgetSettings(Model):
    enabled: bool
    """Whether the widget is enabled."""

    channel_id: Snowflake
    """The widget channel ID."""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
    }
