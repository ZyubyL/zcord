from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class DefaultReaction(Model):
    emoji_id: Snowflake | None = None
    """The ID of a guild's custom emoji."""

    emoji_name: str | None = None
    """The unicode character of the emoji."""

    _transforms: ClassVar[dict[str, Any]] = {
        "emoji_id": Snowflake,
    }
