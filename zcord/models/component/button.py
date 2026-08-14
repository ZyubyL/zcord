from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING, Any, ClassVar

from zcord.enums.component import ButtonStyle, ComponentType
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
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

    @classmethod
    def new(
        cls,
        *,
        style: ButtonStyle = ButtonStyle.SECONDARY,
        label: str | MISSING = MISSING,
        # emoji: Any | MISSING = MISSING,
        custom_id: str | MISSING = MISSING,
        sku_id: Snowflake | MISSING = MISSING,
        url: str | MISSING = MISSING,
        disabled: bool = False,
    ) -> Button:
        """*|classmethod|*

        Create a new button.
        """
        return (
            cls(
                custom_id=custom_id,
                # emoji=emoji,
                # sku_id=sku_id,
            )
            .set_style(style)
            .set_label(label)
            .set_disabled(disabled)
            .set_url(url)
        )

    def _to_payload(self) -> dict:
        if self.style == ButtonStyle.LINK and self.url is MISSING:
            raise ZcordError("URL button must have a URL.")
        if self.url is not MISSING and self.custom_id is not MISSING:
            raise ZcordError("Cannot set both URL and custom ID on a button.")
        if self.style != ButtonStyle.LINK and self.custom_id is MISSING:
            raise ZcordError("Custom ID is required for non-URL buttons.")
        return ZcordModel._to_payload(self)

    def set_custom_id(self, custom_id: str) -> Button:
        """
        Set the custom ID of the button.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ZcordError("Custom ID must be 100 characters or less.")
        return replace(self, custom_id=custom_id)

    def set_style(self, style: ButtonStyle = ButtonStyle.SECONDARY) -> Button:
        """
        Set the style of the button.
        """
        return replace(self, style=style)

    def set_label(self, label: str | MISSING = MISSING) -> Button:
        """
        Set the label of the button.
        """
        if label is not MISSING and (len(label) > 80 or len(label) < 1):
            raise ZcordError("Label must be 80 characters or less.")
        return replace(self, label=label)

    def set_emoji(self, emoji: Any) -> Button:
        """
        Set the emoji of the button.
        """
        raise NotImplementedError

    def set_url(self, url: str | MISSING = MISSING) -> Button:
        """
        Set the URL of the button.
        """
        if url is not MISSING and len(url) > 512:
            raise ZcordError("URL must be 512 characters or less.")
        return replace(self, url=url)

    def set_disabled(self, disabled: bool = False) -> Button:
        """
        Set the disabled state of the button.
        """
        return replace(self, disabled=disabled)


Component._registry[ComponentType.BUTTON] = Button
