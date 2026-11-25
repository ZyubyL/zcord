from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class FollowedChannel(Model):
    channel_id: Snowflake
    """Source channel ID."""

    webhook_id: Snowflake
    """Created target webhook ID."""

    _transforms: ClassVar[dict[str, Any]] = {
        "channel_id": Snowflake,
        "webhook_id": Snowflake,
    }
