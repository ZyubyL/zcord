from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from zcord.cdn import CDN
from zcord.models.base import Model

if TYPE_CHECKING:
    from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AvatarDecorationData(Model):
    """
    Contain data for the user's avatar decoration.

    Attributes:
        asset:
            The avatar decoration hash.
        sku_id:
            The SKU ID of the avatar decoration.
    """

    asset: str
    sku_id: Snowflake

    def asset_url(self, size: int = CDN.MAX_SIZE) -> str:
        """
        The URL of the avatar decoration asset.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        return CDN.avatar_decoration(hash=self.asset, size=size)
