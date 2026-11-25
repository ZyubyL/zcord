from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild.guild_member import GuildMember
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ThreadMember(Model):
    join_timestamp: datetime
    """Time the user last joined the thread."""

    flags: int
    """Any user-thread setting.

    Notes:
        This field currently is only used for notifications.
    """

    member: GuildMember
    """Additional information about the user."""

    id: Snowflake | MISSING = MISSING
    """ID of the thread."""

    user_id: Snowflake | MISSING = MISSING
    """ID of the user."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "user_id": Snowflake,
        "join_timestamp": datetime.fromisoformat,
        "member": GuildMember,
    }
