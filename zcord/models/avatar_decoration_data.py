from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import cdn
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class AvatarDecorationData(Model):
    """Contain data for the user's avatar decoration."""

    asset: str
    """The avatar decoration hash."""

    sku_id: Snowflake
    """The SKU ID of the avatar decoration."""

    _transforms: ClassVar[dict] = {
        "sku_id": Snowflake,
    }

    def asset_url(self, size: int = cdn.MAX_SIZE) -> str:
        """
        The URL of the avatar decoration asset.
        """
        return cdn.avatar_decoration(hash=self.asset, size=size)
