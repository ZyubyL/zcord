from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.interaction.interaction_data.base import InteractionData


@dataclass(frozen=True, slots=True)
class ComponentInteractionData(InteractionData):
    """
    Data for a \
    [`MESSAGE_COMPONENT`][zcord.enums.InteractionType.MESSAGE_COMPONENT] \
    interaction.
    """

    custom_id: str
    """
    The custom ID of the component.
    """

    component_type: enums.ComponentType
    """
    The type of the component.
    """

    values: tuple[str, ...] | MISSING = MISSING
    """
    The values selected in a select menu component.
    """

    _transforms: ClassVar[dict] = {
        "component_type": enums.ComponentType,
    }


InteractionData._registry[enums.InteractionType.MESSAGE_COMPONENT] = (
    ComponentInteractionData
)
