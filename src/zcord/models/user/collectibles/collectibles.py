from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import cdn, types
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.user.collectibles.nameplate import Nameplate


@dataclass(frozen=True, slots=True)
class Collectibles(Model):
    """Contain info about the user's collectibles."""

    nameplate: Nameplate | MISSING = MISSING
    """The user's nameplate."""

    _transforms: ClassVar[dict[str, Any]] = {
        "nameplate": Nameplate,
    }

    def nameplate_url(
        self,
        size: int = cdn.MAX_SIZE,
        format: types.ImageFormat | None = None,
    ) -> str | None:
        """The URL of the user's nameplate."""
        if self.nameplate is MISSING:
            return None

        return self.nameplate.url(size=size, format=format)
