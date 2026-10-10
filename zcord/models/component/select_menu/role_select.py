from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import enums
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import AutoPopulatedSelect


@dataclass(frozen=True, slots=True)
class RoleSelect(AutoPopulatedSelect):
    """A role select menu component"""

    type: enums.ComponentType = enums.ComponentType.ROLE_SELECT

    _default_value_type: ClassVar[Literal["user", "role", "channel"]] = "role"


Component._registry[enums.ComponentType.ROLE_SELECT] = RoleSelect
