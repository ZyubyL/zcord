from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
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
