from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.avatar_decoration_data import AvatarDecorationData
from zcord.models.base import Model
from zcord.models.collectibles import Collectibles
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Member(Model):
    """
    Represent a member of a guild.
    """

    roles: tuple[Snowflake, ...]
    """
    The member's role IDs.
    """

    deaf: bool
    """
    Whether the member is deafened.
    """

    mute: bool
    """
    Whether the member is muted.
    """

    flags: int
    """
    The member's flags.
    """

    permissions: str
    """
    Total permissions of the member in the channel, including overwrites.
    """

    user: User | MISSING = MISSING
    """
    The user associated with this member.
    """

    nick: str | None | MISSING = MISSING
    """
    The nickname of this member.
    """

    avatar: str | None | MISSING = MISSING
    """
    The member's guild avatar hash.
    """

    banner: str | None | MISSING = MISSING
    """
    The member's guild banner hash.
    """

    joined_at: datetime | None = None
    """
    The member's join date.
    """

    premium_since: datetime | None | MISSING = MISSING
    """
    When the member started boosting the guild.
    """

    pending: bool | MISSING = MISSING
    """
    Whether the user has not yet passed the Membership screening requirements.
    """

    communication_disabled_until: datetime | None | MISSING = MISSING
    """
    When the user's timeout will expire.
    """

    avatar_decoration_data: AvatarDecorationData | None | MISSING = MISSING
    """
    The member's guild avatar decoration data.
    """

    collectibles: Collectibles | None | MISSING = MISSING
    """
    The member's collectibles.
    """

    _transforms: ClassVar[dict] = {
        "roles": Snowflake,
        "flags": bitfields.MemberFlags,
        "user": User,
        "joined_at": datetime.fromisoformat,
        "premium_since": datetime.fromisoformat,
        "communication_disabled_until": datetime.fromisoformat,
        "avatar_decoration_data": AvatarDecorationData,
        "collectibles": Collectibles,
    }
