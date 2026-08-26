from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass
class DefaultReaction(Model):
    """
    Represent the emoji to use as the default way to react to a forum post.
    """

    emoji_id: Snowflake | None = None
    """
    The ID of a guild's custom emoji.
    """

    emoji_name: str | None = None
    """
    The unicode character of the emoji.
    """

    _transforms: ClassVar[dict] = {
        "emoji_id": Snowflake,
    }
