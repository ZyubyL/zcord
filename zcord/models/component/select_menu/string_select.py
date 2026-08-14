from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, ClassVar

from zcord.enums.component import ComponentType
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.component.base import Component
from zcord.types import SelectMenu


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


@dataclass(frozen=True, slots=True)
class StringSelect(Component, SelectMenu):
    """
    A string select menu that holds a list of max to 25 options.

    Attributes:
        custom_id:
            The custom ID of the select menu.
        options:
            A list of select options.
        placeholder:
            The placeholder text of the select menu.
        min_values:
            The minimum number of values that can be selected.
        max_values:
            The maximum number of values that can be selected.
        required:
            Whether the select menu is required.
        disabled:
            Whether the select menu is disabled.

    Notes:
        - If `required` is True or [`MISSING`][], `min_values` must be 1 \
        or [`MISSING`][].
        - `required` is only available for [`Modal`][].

    Warning:
        - You can't use `disabled` with [`Modal`][].
    """

    type: ComponentType = ComponentType.STRING_SELECT
    custom_id: str | MISSING = MISSING
    options: list[SelectOption] | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    min_values: int | MISSING = MISSING
    max_values: int | MISSING = MISSING
    required: bool | MISSING = MISSING
    disabled: bool | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "options": SelectOption,
    }

    @classmethod
    def new(
        cls,
        *,
        custom_id: str | MISSING = MISSING,
        options: list[SelectOption] | MISSING = MISSING,
        placeholder: str | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> StringSelect:
        """*|classmethod|*

        Create a new string select component.
        """
        return (
            cls(
                custom_id=custom_id,
                options=options,
            )
            .set_placeholder(placeholder)
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
        )

    def set_custom_id(self, custom_id: str) -> StringSelect:
        """
        Set the custom ID of the string select component.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ZcordError("Custom ID cannot be longer than 100 characters.")
        return replace(self, custom_id=custom_id)

    def set_options(self, options: list[SelectOption]) -> StringSelect:
        """
        Set the options of the string select component.
        """
        select = self.clear_options()
        return select.add_options(options)

    def add_options(self, options: list[SelectOption]) -> StringSelect:
        """
        Add options to the string select component.
        """
        select = self
        for option in options:
            select = select.add_option(option)
        return select

    def add_option(self, option: SelectOption) -> StringSelect:
        """
        Add an option to the string select component.
        """
        if self.options is MISSING:
            return replace(self, options=[option])
        if len(self.options) + 1 > 25:
            raise ZcordError(
                "String select component cannot have more than 25 options."
            )
        return replace(
            self,
            options=[*self.options, option]
            if self.options is not MISSING
            else [option],
        )

    def clear_options(self) -> StringSelect:
        """
        Clear the options of the string select component.
        """
        return replace(self, options=MISSING)

    def set_placeholder(self, placeholder: str | MISSING) -> StringSelect:
        """
        Set the placeholder of the string select component.
        """
        if placeholder is not MISSING and len(placeholder) > 150:
            raise ZcordError(
                "Placeholder cannot be longer than 150 characters."
            )
        return replace(self, placeholder=placeholder)

    def set_min_values(self, min_values: int) -> StringSelect:
        """
        Set the minimum number of values that can be selected.
        """
        if min_values < 1 or min_values > 25:
            raise ZcordError("min_values must be between 1 and 25.")
        return replace(self, min_values=min_values)

    def set_max_values(self, max_values: int) -> StringSelect:
        """
        Set the maximum number of values that can be selected.
        """
        if max_values < 1 or max_values > 25:
            raise ZcordError("max_values must be between 1 and 25.")
        return replace(self, max_values=max_values)

    def set_required(self, required: bool) -> StringSelect:
        """
        Set whether the string select component is required.
        """
        return replace(self, required=required)

    def set_disabled(self, disabled: bool) -> StringSelect:
        """
        Set whether the string select component is disabled.
        """
        return replace(self, disabled=disabled)


Component._registry[ComponentType.STRING_SELECT] = StringSelect
