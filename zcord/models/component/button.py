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
