from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import add_field_value, set_field_value
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import SelectMenu
from zcord.models.component.select_menu.select_option import SelectOption

if TYPE_CHECKING:
    from zcord import types


@dataclass(frozen=True, slots=True)
class StringSelect(SelectMenu):
    """
    A string select menu that holds a list of max to 25 options.

    Notes:
        - If `required` is True or [`MISSING`][zcord.MISSING], \
        `min_values` must be 1 or [`MISSING`][zcord.MISSING].
        - `required` is only available for [`Modal`][].

    Warning:
        - You can't use `disabled` with [`Modal`][].
    """

    type: enums.ComponentType = enums.ComponentType.STRING_SELECT

    options: tuple[SelectOption, ...] | MISSING = MISSING
    """
    A list of select options.
    """

    _transforms: ClassVar[dict] = {
        "type": enums.ComponentType,
        "options": SelectOption,
    }

    @classmethod
    def new(
        cls,
        *,
        custom_id: str | MISSING = MISSING,
        options: types.TupleOrList[SelectOption] | MISSING = MISSING,
        placeholder: str | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> StringSelect:
        """
        Create a new string select component.

        Raises:
            ValueError:
                - placeholder cannot be longer than 150 characters.
                - options cannot have more than 25 options.
        """
        return (
            cls(custom_id=custom_id)
            .set_placeholder(placeholder)
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
            .set_options(options)
        )

    def set_options(
        self,
        options: types.TupleOrList[SelectOption] | MISSING = MISSING,
    ) -> StringSelect:
        """
        Set the options of the string select component.

        Raises:
            ValueError:
                String select component cannot have more than 25 options.
        """
        select = self.clear_options()
        if options is MISSING:
            return select

        return select.add_options(*options)

    def add_options(self, *options: SelectOption) -> StringSelect:
        """
        Add options to the string select component.

        Raises:
            ValueError:
                String select component cannot have more than 25 options.
        """
        select = self
        for option in options:
            select = select.add_option(option)
        return select

    def add_option(self, option: SelectOption) -> StringSelect:
        """
        Add an option to the string select component.

        Raises:
            ValueError:
                String select component cannot have more than 25 options.
        """
        if self.options is not MISSING and len(self.options) >= 25:
            raise ValueError(
                "String select component cannot have more than 25 options."
            )
        return add_field_value(self, "options", option)

    def clear_options(self) -> StringSelect:
        """
        Clear the options of the string select component.
        """
        return set_field_value(self, "options", MISSING)


Component._registry[enums.ComponentType.STRING_SELECT] = StringSelect
