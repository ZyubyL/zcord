from __future__ import annotations

from dataclasses import dataclass

from zcord import enums
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import AutoPopulatedSelect


@dataclass(frozen=True, slots=True)
class MentionableSelect(AutoPopulatedSelect):
    """A mentionable select menu component"""

    type: enums.ComponentType = enums.ComponentType.MENTIONABLE_SELECT


Component._registry[enums.ComponentType.MENTIONABLE_SELECT] = MentionableSelect
