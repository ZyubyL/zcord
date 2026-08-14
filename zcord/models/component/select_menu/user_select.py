from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord.enums.component import ComponentType
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.component.base import Component
from zcord.models.component.select_menu.default_value import DefaultValue
from zcord.types import SelectMenu


@dataclass(frozen=True, slots=True)
class UserSelect(Component, SelectMenu):
    """
    A user select menu component.

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

    type: ComponentType = ComponentType.USER_SELECT
    custom_id: str | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    default_values: list[DefaultValue] | MISSING = MISSING
    min_values: int | MISSING = MISSING
    max_values: int | MISSING = MISSING
    required: bool | MISSING = MISSING
    disabled: bool | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "default_values": DefaultValue,
    }

    @classmethod
    def new(
        cls,
        *,
        custom_id: str,
        placeholder: str | MISSING = MISSING,
        default_values: list[DefaultValue] | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> UserSelect:
        return (
            cls(
                custom_id=custom_id,
                placeholder=placeholder,
                default_values=default_values,
            )
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
        )

    def set_custom_id(self, custom_id: str) -> UserSelect:
        """
        Set the custom ID of the string select component.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ZcordError("Custom ID cannot be longer than 100 characters.")
        return replace(self, custom_id=custom_id)

    def set_placeholder(self, placeholder: str | MISSING) -> UserSelect:
        """
        Set the placeholder of the user select component.
        """
        if placeholder is not MISSING and len(placeholder) > 150:
            raise ZcordError(
                "Placeholder cannot be longer than 150 characters."
            )
        return replace(self, placeholder=placeholder)

    def set_default_values(
        self, default_values: list[DefaultValue]
    ) -> UserSelect:
        """
        Set the default values of the user select component.
        """
        select = self.clear_default_values()
        return select.add_default_values(default_values)

    def add_default_values(
        self, default_values: list[DefaultValue]
    ) -> UserSelect:
        """
        Add default values to the user select component.
        """
        select = self
        for value in default_values:
            select = select.add_default_value(value)
        return select

    def add_default_value(self, default_value: DefaultValue) -> UserSelect:
        """
        Add a default value to the user select component.
        """
        return replace(
            self,
            default_values=[*self.default_values, default_value]
            if self.default_values is not MISSING
            else [default_value],
        )

    def clear_default_values(self) -> UserSelect:
        """
        Clear all default values from the user select component.
        """
        return replace(self, default_values=MISSING)

    def set_min_values(self, min_values: int) -> UserSelect:
        """
        Set the minimum number of values that can be selected.
        """
        if min_values < 1 or min_values > 25:
            raise ZcordError("min_values must be between 1 and 25.")
        return replace(self, min_values=min_values)

    def set_max_values(self, max_values: int) -> UserSelect:
        """
        Set the maximum number of values that can be selected.
        """
        if max_values < 1 or max_values > 25:
            raise ZcordError("max_values must be between 1 and 25.")
        return replace(self, max_values=max_values)

    def set_required(self, required: bool) -> UserSelect:
        """
        Set whether the user select component is required.
        """
        return replace(self, required=required)

    def set_disabled(self, disabled: bool) -> UserSelect:
        """
        Set whether the user select component is disabled.
        """
        return replace(self, disabled=disabled)


Component._registry[ComponentType.USER_SELECT] = UserSelect
