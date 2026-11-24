from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


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
