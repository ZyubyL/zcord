from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING, ClassVar

from zcord.enums.component import ButtonStyle, ComponentType
from zcord.missing import MISSING
from zcord.models.component.base import Component
from zcord.models.emoji import Emoji

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
    emoji: Emoji | MISSING = MISSING
    custom_id: str | MISSING = MISSING
    sku_id: Snowflake | MISSING = MISSING
    url: str | MISSING = MISSING
    disabled: bool = False

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "style": ButtonStyle,
        "emoji": Emoji,
    }

    @classmethod
    def new(
        cls,
        *,
        style: ButtonStyle = ButtonStyle.SECONDARY,
        label: str | MISSING = MISSING,
        emoji: Emoji | MISSING = MISSING,
        custom_id: str | MISSING = MISSING,
        # sku_id: Snowflake | MISSING = MISSING,
        url: str | MISSING = MISSING,
        disabled: bool = False,
    ) -> Button:
        """*|classmethod|*

        Create a new button.

        Raises:
            ValueError:
                - Custom ID must be 100 characters or less \
                (if it is not a link button).
                - Label must be 80 characters or less.
                - URL must be 512 characters or less (if it is a link button).
        """
        return (
            cls(
                custom_id=custom_id,
                # sku_id=sku_id,
            )
            .set_style(style)
            .set_label(label)
            .set_disabled(disabled)
            .set_url(url)
            .set_emoji(emoji)
        )

    def _check_before(self) -> None:
        if self.style == ButtonStyle.LINK and self.url is MISSING:
            raise ValueError("URL button must have a URL.")
        if self.url is not MISSING and self.custom_id is not MISSING:
            raise ValueError("Cannot set both URL and custom ID on a button.")
        if self.style != ButtonStyle.LINK and self.custom_id is MISSING:
            raise ValueError("Custom ID is required for non-URL buttons.")

    def set_custom_id(self, custom_id: str) -> Button:
        """
        Set the custom ID of the button.

        Raises:
            ValueError:
                Custom ID must be 100 characters or less.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ValueError("Custom ID must be 100 characters or less.")
        return replace(self, custom_id=custom_id)

    def set_style(self, style: ButtonStyle = ButtonStyle.SECONDARY) -> Button:
        """
        Set the style of the button.
        """
        return replace(self, style=style)

    def set_label(self, label: str | MISSING = MISSING) -> Button:
        """
        Set the label of the button.

        Raises:
            ValueError:
                Label must be 80 characters or less.
        """
        if label is not MISSING and (len(label) > 80 or len(label) < 1):
            raise ValueError("Label must be 80 characters or less.")
        return replace(self, label=label)

    def set_emoji(self, emoji: Emoji | str | MISSING = MISSING) -> Button:
        """
        Set the emoji of the button.
        """
        return replace(
            self,
            emoji=emoji
            if isinstance(emoji, Emoji)
            else Emoji.new(emoji)
            if emoji is not MISSING
            else MISSING,
        )

    def set_url(self, url: str | MISSING = MISSING) -> Button:
        """
        Set the URL of the button.

        Raises:
            ValueError:
                URL must be 512 characters or less.
        """
        if url is not MISSING and len(url) > 512:
            raise ValueError("URL must be 512 characters or less.")
        return replace(self, url=url)

    def set_disabled(self, disabled: bool = False) -> Button:
        """
        Set the disabled state of the button.
        """
        return replace(self, disabled=disabled)


Component._registry[ComponentType.BUTTON] = Button
