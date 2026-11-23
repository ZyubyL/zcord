from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class TeamMember(Model):
    """Represent a developer team member."""

    membership_state: enums.MembershipState
    """User's membership state on the team."""

    team_id: Snowflake
    """ID of the team they are a member of."""

    user: User
    """User object of this team member."""

    role: str
    """Role of this team member."""

    _transforms: ClassVar[dict[str, Any]] = {
        "membership_state": enums.MembershipState,
        "team_id": Snowflake,
        "user": User,
    }
