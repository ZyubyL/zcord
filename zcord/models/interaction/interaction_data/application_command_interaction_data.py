from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import enums
from zcord.models.interaction.interaction_data.base import InteractionData
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ApplicationCommandInteractionData(InteractionData):
    """
    Data for an \
    [`APPLICATION_COMMAND`][zcord.enums.InteractionType.APPLICATION_COMMAND] \
    interaction.
    """

    id: Snowflake
    """
    The ID of the invoked command.
    """

    name: str
    """
    The name of the invoked command.
    """

    type: int
    """
    The type of the invoked command.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }


InteractionData._registry[enums.InteractionType.APPLICATION_COMMAND] = (
    ApplicationCommandInteractionData
)
