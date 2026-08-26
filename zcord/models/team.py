from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import enums
from zcord.cdn import CDN
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class TeamMember:
    """
    Represent a developer team member.
    """

    membership_state: enums.MembershipState
    """
    The user's membership state on the team.
    """

    team_id: Snowflake
    """
    The team's ID.
    """

    user: User
    """
    The user associated with this team member.
    """

    role: str
    """
    The role of the user on the team.
    """

    _transforms: ClassVar[dict] = {
        "membership_state": enums.MembershipState,
        "team_id": Snowflake,
        "user": User,
    }


@dataclass(frozen=True, slots=True)
class Team(Model):
    """
    Represent a developer team.
    """

    id: Snowflake
    """
    The team's ID.
    """

    name: str
    """
    The team's name.
    """

    owner_user_id: Snowflake
    """
    The [`User`][] ID of the team's owner.
    """

    members: tuple[TeamMember, ...]
    """
    A list of team members.
    """

    icon: str | None = None
    """
    The team's icon hash.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "owner_user_id": Snowflake,
        "members": TeamMember,
    }

    def icon_url(
        self,
        *,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp"] | None = None,
    ) -> str | None:
        """
        The team's icon URL.
        """
        if self.icon is None:
            return None
        return CDN.team_icon(
            team_id=self.id,
            hash=self.icon,
            size=size,
            format=format,
        )
