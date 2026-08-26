from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import SelectMenu
from zcord.models.component.select_menu.default_value import DefaultValue


@dataclass(frozen=True, slots=True)
class UserSelect(SelectMenu):
    """
    A user select menu component.

    Notes:
        - If `required` is True or [`MISSING`][], `min_values` must be 1 \
        or [`MISSING`][].
        - `required` is only available for [`Modal`][].

    Warning:
        - You can't use `disabled` with [`Modal`][].
    """

    type: enums.ComponentType = enums.ComponentType.USER_SELECT

    placeholder: str | MISSING = MISSING
    """
    The placeholder text of the select menu.
    """

    default_values: tuple[DefaultValue] | MISSING = MISSING
    """
    List of default values for auto-populated select menu components.
    """

    _transforms: ClassVar[dict] = {
        "type": enums.ComponentType,
        "default_values": DefaultValue,
    }

    @classmethod
    def new(
        cls,
        *,
        custom_id: str | MISSING = MISSING,
        placeholder: str | MISSING = MISSING,
        default_values: tuple[DefaultValue, ...]
        | list[DefaultValue]
        | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> UserSelect:
        return (
            cls(custom_id=custom_id)
            .set_placeholder(placeholder)
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
            .set_default_values(default_values)
        )

    def set_placeholder(
        self, placeholder: str | MISSING = MISSING
    ) -> UserSelect:
        """
        Set the placeholder of the user select component.

        Raises:
            ValueError:
                Placeholder cannot be longer than 150 characters.
        """
        if placeholder is not MISSING and len(placeholder) > 150:
            raise ValueError(
                "Placeholder cannot be longer than 150 characters."
            )
        return replace(self, placeholder=placeholder)

    def set_default_values(
        self,
        default_values: tuple[DefaultValue, ...]
        | list[DefaultValue]
        | MISSING = MISSING,
    ) -> UserSelect:
        """
        Set the default values of the user select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        select = self.clear_default_values()
        if default_values is MISSING:
            return select

        default_values = [replace(dv, type="user") for dv in default_values]
        return select.add_default_values(default_values)

    def add_default_values(
        self, default_values: tuple[DefaultValue, ...] | list[DefaultValue]
    ) -> UserSelect:
        """
        Add default values to the user select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        select = self
        for value in default_values:
            select = select.add_default_value(value)
        return select

    def add_default_value(self, default_value: DefaultValue) -> UserSelect:
        """
        Add a default value to the user select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        return replace(
            self,
            default_values=(*self.default_values, default_value)
            if self.default_values is not MISSING
            else (default_value,),
        )

    def clear_default_values(self) -> UserSelect:
        """
        Clear all default values from the user select component.
        """
        return replace(self, default_values=MISSING)


Component._registry[enums.ComponentType.USER_SELECT] = UserSelect
