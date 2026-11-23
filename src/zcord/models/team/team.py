from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar

from zcord import cdn
from zcord.models.base import Model
from zcord.models.team import TeamMember
from zcord.snowflake import Snowflake

if TYPE_CHECKING:
    from zcord import types


@dataclass(frozen=True, slots=True)
class Team(Model):
    """Represent a developer team."""

    id: Snowflake
    """Unique ID of the team."""

    name: str
    """Name of the team."""

    owner_user_id: Snowflake
    """User ID of the current team owner."""

    members: tuple[TeamMember, ...]
    """Members of the team."""

    icon: str | None = None
    """Team's icon image hash."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "owner_user_id": Snowflake,
        "members": TeamMember,
    }

    def icon_url(
        self,
        *,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The team's icon URL."""
        if self.icon is None:
            return None
        return cdn.team_icon(
            team_id=int(self.id),
            hash=self.icon,
            size=size,
            format=format,
        )
