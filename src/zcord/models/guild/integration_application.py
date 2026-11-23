from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import cdn, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.user.user import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class IntegrationApplication(Model):
    id: Snowflake
    """The ID of the app."""

    name: str
    """The name of the app."""

    description: str
    """The description of the app."""

    icon: str | None = None
    """The icon hash of the app."""

    bot: User | MISSING = MISSING
    """The bot associated with this application."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "bot": User,
    }

    def icon_url(
        self,
        *,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The application icon URL if available."""
        if not self.icon:
            return None
        return cdn.application_icon_cover(
            app_id=self.id,
            hash=self.icon,
            size=size,
            format=format,
        )
