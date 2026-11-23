from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Literal

from zcord import cdn, errors, types
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Nameplate(Model):
    """Contain info about the user's nameplate."""

    sku_id: Snowflake
    """The ID of the nameplate SKU."""

    asset: str
    """Path to the nameplate asset."""

    label: str
    """The label of the nameplate[^1].

    [^1]: This field is unused.
    """

    palette: Literal[
        "crimson",
        "berry",
        "sky",
        "teal",
        "forest",
        "bubble_gum",
        "violet",
        "cobalt",
        "clover",
        "lemon",
        "white",
    ]
    """The background color of the nameplate."""

    _transforms: ClassVar[dict[str, Any]] = {
        "sku_id": Snowflake,
    }

    def url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str:
        raise errors.ZcordError(
            """Discord doesn't provide nameplate URL.
            So this will raise an error until they update their docs."""
        )
