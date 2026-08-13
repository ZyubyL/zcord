from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from zcord.cdn import CDN
from zcord.models.base import ZcordModel

if TYPE_CHECKING:
    from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AvatarDecorationData(ZcordModel):
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

    @property
    def asset_url(self) -> str:
        """
        The URL of the avatar decoration asset.
        """
        return CDN.avatar_decoration(self.asset)
