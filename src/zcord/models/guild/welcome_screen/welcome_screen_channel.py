from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class WelcomeScreenChannel(Model):
    channel_id: Snowflake
    """The channel's ID."""

    description: str
    """The description shown for the channel."""

    emoji_id: Snowflake | None = None
    """The emoji ID, if the emoji is custom."""

    emoji_name: str | None = None
    """The emoji name if custom, the unicode character if standard, \
    or [`None`][] if no emoji is set."""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
        "emoji_id": Snowflake,
    }
