from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.member import Member
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ThreadMember(Model):
    """
    Contain info about a user that has joined a thread.
    """

    join_timestamp: datetime
    """
    The timestamp when the user last joined the thread.
    """

    flags: int
    """
    Any user's thread settings.[^1]

    [^1]: https://docs.discord.com/developers/resources/channel#thread-member-object
    """

    id: Snowflake | MISSING = MISSING
    """
    The thread's ID.
    """

    user_id: Snowflake | MISSING = MISSING
    """
    The user's ID.
    """

    member: Member | MISSING = MISSING
    """
    Additional info about the user.
    """

    _transforms: ClassVar[dict] = {
        "join_timestamp": datetime.fromisoformat,
        "id": Snowflake,
        "user_id": Snowflake,
        "member": Member,
    }
