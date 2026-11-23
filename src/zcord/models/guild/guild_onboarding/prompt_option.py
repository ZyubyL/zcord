from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.emoji import Emoji
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class PromptOption(Model):
    id: Snowflake
    """ID of the prompt option."""

    channel_ids: tuple[Snowflake, ...]
    """IDs for channels a member is added to when the option is selected."""

    role_ids: tuple[Snowflake, ...]
    """IDS for roles assigned to a member when the option is selected."""

    emoji_id: Snowflake
    """Emoji ID of the option."""

    emoji_animated: bool
    """Whether the emoji is animated."""

    title: str
    """Title of the option."""

    description: str | None
    """Description of the option."""

    emoji: Emoji | MISSING = MISSING
    """Emoji of the option."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "channel_ids": Snowflake,
        "role_ids": Snowflake,
        "emoji_id": Snowflake,
        "emoji": Emoji,
    }
