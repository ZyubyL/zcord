from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord.enums.component import ComponentType
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import SelectMenu
from zcord.models.component.select_menu.select_option import SelectOption


@dataclass(frozen=True, slots=True)
class StringSelect(SelectMenu):
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
    options: tuple[SelectOption, ...] | MISSING = MISSING
    placeholder: str | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "options": SelectOption,
    }

    @classmethod
    def new(
        cls,
        *,
        custom_id: str | MISSING = MISSING,
        options: tuple[SelectOption, ...]
        | list[SelectOption]
        | MISSING = MISSING,
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
            )
            .set_options(options if options is not MISSING else ())
            .set_placeholder(placeholder)
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
        )

    def set_options(
        self, options: tuple[SelectOption, ...] | list[SelectOption]
    ) -> StringSelect:
        """
        Set the options of the string select component.
        """
        select = self.clear_options()
        return select.add_options(options)

    def add_options(
        self, options: tuple[SelectOption, ...] | list[SelectOption]
    ) -> StringSelect:
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
        if self.options is not MISSING and len(self.options) >= 25:
            raise ZcordError(
                "String select component cannot have more than 25 options."
            )
        return replace(
            self,
            options=(*self.options, option)
            if self.options is not MISSING
            else (option,),
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


Component._registry[ComponentType.STRING_SELECT] = StringSelect
