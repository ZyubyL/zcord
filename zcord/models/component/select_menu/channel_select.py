from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import enums
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import AutoPopulatedSelect


@dataclass(frozen=True, slots=True)
class ChannelSelect(AutoPopulatedSelect):
    """A channel select menu component"""

    type: enums.ComponentType = enums.ComponentType.CHANNEL_SELECT

    _default_value_type: ClassVar[Literal["user", "role", "channel"]] = (
        "channel"
    )


Component._registry[enums.ComponentType.CHANNEL_SELECT] = ChannelSelect
