from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.emoji import Emoji


@dataclass(frozen=True, slots=True)
class SelectOption(Model):
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
    emoji: Emoji | MISSING = MISSING
    default: bool = False

    _transforms: ClassVar[dict] = {
        "emoji": Emoji,
    }

    def _check_before(self) -> None:
        if self.label is MISSING or self.value is MISSING:
            raise ValueError("Select option's label and value is required.")
        if not self.label or not self.value:
            raise ValueError(
                "Select option's label and value must not be empty."
            )

    @classmethod
    def new(
        cls,
        *,
        label: str | MISSING = MISSING,
        value: str | MISSING = MISSING,
        description: str | MISSING = MISSING,
        emoji: Emoji | MISSING = MISSING,
        default: bool = False,
    ) -> SelectOption:
        """*|classmethod|*

        Create a select option for a string select menu.
        """
        return (
            cls()
            .set_description(description)
            .set_default(default)
            .set_label(label)
            .set_value(value)
            .set_emoji(emoji)
        )

    def set_label(self, label: str | MISSING = MISSING) -> SelectOption:
        """
        Set the label of the select option.

        Raises:
            ValueError:
                Label must be between 1 and 100 characters.
        """
        if label is not MISSING and (len(label) > 100 or len(label) < 1):
            raise ValueError("Label must be between 1 and 100 characters.")
        return replace(self, label=label)

    def set_value(self, value: str | MISSING = MISSING) -> SelectOption:
        """
        Set the value of the select option.

        Raises:
            ValueError:
                Value must be between 1 and 100 characters.
        """
        if value is not MISSING and (len(value) > 100 or len(value) < 1):
            raise ValueError("Value must be between 1 and 100 characters.")
        return replace(self, value=value)

    def set_description(
        self, description: str | MISSING = MISSING
    ) -> SelectOption:
        """
        Set the description of the select option.

        Raises:
            ValueError:
                Description must be between 1 and 100 characters.
        """
        if description is not MISSING and len(description) > 100:
            raise ValueError(
                "Description must be between 1 and 100 characters."
            )
        return replace(self, description=description)

    def set_emoji(self, emoji: Emoji | MISSING = MISSING) -> SelectOption:
        """
        Set the emoji of the select option.
        """
        return replace(self, emoji=emoji)

    def set_default(self, default: bool) -> SelectOption:
        """
        Set whether showing this option as selected by default.
        """
        return replace(self, default=default)
