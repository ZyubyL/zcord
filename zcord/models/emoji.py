from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.cdn import CDN
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass
class Emoji(ZcordModel):
    """
    Represent a Discord emoji.

    Attributes:
        id:
            The ID of the emoji.
        name:
            The name of the emoji.
        roles:
            A list of role IDs that the emoji is restricted to.
        user:
            The user who created the emoji.
        require_colons:
            Whether the emoji requires colons to be used.
        managed:
            Whether the emoji is managed.
        animated:
            Whether the emoji is animated.
        available:
            Whether the emoji is available.
    """

    id: Snowflake | None = None
    name: str | None = None
    roles: list[Snowflake] | MISSING = MISSING
    user: User | MISSING = MISSING
    require_colons: bool | MISSING = MISSING
    managed: bool | MISSING = MISSING
    animated: bool | MISSING = MISSING
    available: bool | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "roles": Snowflake,
        "user": User,
    }

    def url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the emoji.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.id is None:
            return None
        return CDN.emoji(
            hash=str(self.id),
            size=size,
            format=format,
        )
