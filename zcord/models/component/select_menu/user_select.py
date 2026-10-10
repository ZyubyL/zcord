from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import enums
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import AutoPopulatedSelect


@dataclass(frozen=True, slots=True)
class UserSelect(AutoPopulatedSelect):
    """
    A user select menu component.

    Notes:
        - If `required` is True or [`MISSING`][zcord.MISSING], \
        `min_values` must be 1 or [`MISSING`][zcord.MISSING].
        - `required` is only available for [`Modal`][].

    Warning:
        - You can't use `disabled` with [`Modal`][].
    """

    type: enums.ComponentType = enums.ComponentType.USER_SELECT

    _default_value_type: ClassVar[Literal["user", "role", "channel"]] = "user"


Component._registry[enums.ComponentType.USER_SELECT] = UserSelect
