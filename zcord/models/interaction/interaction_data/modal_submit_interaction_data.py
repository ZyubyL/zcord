from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from zcord import enums
from zcord.models.interaction.interaction_data.base import InteractionData

if TYPE_CHECKING:
    from zcord.models.component.base import Component


@dataclass(frozen=True, slots=True)
class ModalSubmitInteractionData(InteractionData):
    """
    Data for a [`MODAL_SUBMIT`][zcord.enums.InteractionType.MODAL_SUBMIT] \
    interaction.
    """

    custom_id: str
    """
    The custom ID of the modal.
    """

    components: tuple[Component, ...] = ()
    """
    The components submitted with the modal.
    """


InteractionData._registry[enums.InteractionType.MODAL_SUBMIT] = (
    ModalSubmitInteractionData
)
