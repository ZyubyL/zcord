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

    Attributes:
        sku_id:
            The ID of the nameplate SKU.
        asset:
            Path to the nameplate asset.
        label:
            The label of the nameplate. (Unused)
        palette:
            The background color of the nameplate.
    """

    sku_id: Snowflake
    asset: str
    label: str
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
    Contains info about the user's collectibles.

    Attributes:
        nameplate:
            The user's nameplate.
    """

    nameplate: Nameplate | MISSING = MISSING

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
