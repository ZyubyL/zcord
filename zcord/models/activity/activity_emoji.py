from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ActivityEmoji(Model):
    """Represent the emoji used for a custom status."""

    name: str
    """The name of the emoji."""

    id: Snowflake | MISSING = MISSING
    """The ID of the emoji."""

    animated: bool | MISSING = MISSING
    """Whether the emoji is animated."""

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }
