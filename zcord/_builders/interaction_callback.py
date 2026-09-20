from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from zcord.missing import MISSING
from zcord.models.base import Model

if TYPE_CHECKING:
    from zcord import enums
    from zcord.models.interaction.interaction_data import InteractionData


@dataclass(frozen=True, slots=True)
class _InteractionCallback(Model):
    type: enums.InteractionCallbackType
    data: InteractionData | MISSING = MISSING
