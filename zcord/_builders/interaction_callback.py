from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from zcord.missing import MISSING
from zcord.models.base import Model

if TYPE_CHECKING:
    from zcord import enums


@dataclass(frozen=True, slots=True)
class _InteractionCallback(Model):
    type: enums.InteractionCallbackType
    data: Any | MISSING = MISSING
