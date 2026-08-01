from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar

from zcord.enums.component import ButtonStyle, ComponentType
from zcord.missing import MISSING
from zcord.models.component.base import Component

if TYPE_CHECKING:
    from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Button(Component):
    """
    Represents an interactive button.

    Attributes:
        style:
            The style of the button.
        label:
            The label of the button.
        emoji:
            The emoji of the button.
        custom_id:
            The custom ID of the button.
        sku_id:
            The SKU ID of the button.
        url:
            The URL of the button.
        disabled:
            Whether the button is disabled.
    """

    type: ComponentType = ComponentType.BUTTON
    style: ButtonStyle = ButtonStyle.SECONDARY
    label: str | MISSING = MISSING
    emoji: Any | MISSING = MISSING
    custom_id: str | MISSING = MISSING
    sku_id: Snowflake | MISSING = MISSING
    url: str | MISSING = MISSING
    disabled: bool = False

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "style": ButtonStyle,
    }


Component._registry[ComponentType.BUTTON] = Button
