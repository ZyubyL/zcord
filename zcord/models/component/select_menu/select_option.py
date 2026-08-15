from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any

from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.base import ZcordModel


@dataclass(frozen=True, slots=True)
class SelectOption(ZcordModel):
    """
    A select option for a string select menu.

    Attributes:
        label:
            The bold text displayed on the option.
        value:
            The value under-the-hood of the option.
        description:
            The small text displayed below the label.
        emoji:
            The emoji next to the label.
        default:
            Whether the option is selected by default.
    """

    label: str | MISSING = MISSING
    value: str | MISSING = MISSING
    description: str | MISSING = MISSING
    emoji: Any | MISSING = MISSING
    default: bool = False

    def _to_payload(self) -> dict:
        if self.label is MISSING or self.value is MISSING:
            raise ZcordError("Select option's label and value is required.")
        if not self.label or not self.value:
            raise ZcordError(
                "Select option's label and value must not be empty."
            )
        return ZcordModel._to_payload(self)

    @classmethod
    def new(
        cls,
        *,
        label: str | MISSING = MISSING,
        value: str | MISSING = MISSING,
        description: str | MISSING = MISSING,
        emoji: Any | MISSING = MISSING,
        default: bool = False,
    ) -> SelectOption:
        """*|classmethod|*

        Create a select option for a string select menu.
        """
        return cls(
            label=label,
            value=value,
            description=description,
            emoji=emoji,
            default=default,
        )

    def set_label(self, label: str) -> SelectOption:
        """
        Set the label of the select option.
        """
        if len(label) > 100 or len(label) < 1:
            raise ZcordError("Label must be between 1 and 100 characters.")
        return replace(self, label=label)

    def set_value(self, value: str) -> SelectOption:
        """
        Set the value of the select option.
        """
        if len(value) > 100 or len(value) < 1:
            raise ZcordError("Value must be between 1 and 100 characters.")
        return replace(self, value=value)

    def set_description(
        self, description: str | MISSING = MISSING
    ) -> SelectOption:
        """
        Set the description of the select option.
        """
        if description is not MISSING and len(description) > 100:
            raise ZcordError(
                "Description must be between 1 and 100 characters."
            )
        return replace(self, description=description)

    def set_emoji(self, emoji: Any | MISSING = MISSING) -> SelectOption:
        """
        Set the emoji of the select option.
        """
        raise NotImplementedError

    def set_default(self, default: bool | MISSING = MISSING) -> SelectOption:
        """
        Set whether showing this option as selected by default.
        """
        return replace(self, default=default)
