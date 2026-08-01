from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from zcord.enums.component import ComponentType
from zcord.missing import MISSING
from zcord.models.component.base import Component

if TYPE_CHECKING:
    from zcord.models.component.button import Button
    from zcord.types import SelectMenu


@dataclass(frozen=True, slots=True)
class ActionRow(Component):
    """
    Represent an action row that holds max to 5 buttons or a select menu.

    Attributes:
        components:
            A list of components inside the action row.
    """

    type: ComponentType = ComponentType.ACTION_ROW
    components: list[Button] | SelectMenu | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "components": Component,
    }


Component._registry[ComponentType.ACTION_ROW] = ActionRow
