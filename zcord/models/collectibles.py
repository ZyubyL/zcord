from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.cdn import CDN
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Nameplate(Model):
    """
    Contain info about the user's nameplate.
    """

    sku_id: Snowflake
    """
    The ID of the nameplate SKU.
    """

    asset: str
    """
    Path to the nameplate asset.
    """

    label: str
    """
    The label of the nameplate.[^1]

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
    """
    The background color of the nameplate.
    """

    _transforms: ClassVar[dict] = {
        "sku_id": Snowflake,
    }

    def url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp"] | None = None,
    ) -> str:
        raise ZcordError(
            """
            Discord doesn't provide nameplate URL.
            So this will be the error until they update their docs
            """
        )


@dataclass(frozen=True, slots=True)
class Collectibles(Model):
    """
    Contain info about the user's collectibles.
    """

    nameplate: Nameplate | MISSING = MISSING
    """
    The user's nameplate.
    """

    _transforms: ClassVar[dict] = {
        "nameplate": Nameplate,
    }

    def nameplate_url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp"] | None = None,
    ) -> str | None:
        """
        The URL of the user's nameplate.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.nameplate is MISSING:
            return None

        return self.nameplate.url(size=size, format=format)
