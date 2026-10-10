from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar, Literal, Self

from zcord import enums, types
from zcord.missing import MISSING
from zcord.models.base import add_field_value, set_field_value
from zcord.models.component.base import Component
from zcord.models.component.select_menu.default_value import DefaultValue


@dataclass(frozen=True, slots=True)
class SelectMenu(Component):
    """
    Base class for select menu components.
    Used for type hinting.
    """

    custom_id: str | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    min_values: int | MISSING = MISSING
    max_values: int | MISSING = MISSING
    required: bool | MISSING = MISSING
    disabled: bool | MISSING = MISSING

    def set_custom_id(self, custom_id: str) -> Self:
        """
        Set the custom ID of the select component.

        Raises:
            ValueError:
                Custom ID must be 100 characters or less.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ValueError("Custom ID cannot be longer than 100 characters.")
        return set_field_value(self, "custom_id", custom_id)

    def set_placeholder(self, placeholder: str | MISSING = MISSING) -> Self:
        """
        Set the placeholder of the select menu component.

        Raises:
            ValueError:
                Placeholder cannot be longer than 150 characters.
        """
        if placeholder is not MISSING and len(placeholder) > 150:
            raise ValueError(
                "Placeholder cannnot be longer than 150 characters."
            )
        return set_field_value(self, "placeholder", placeholder)

    def set_min_values(self, min_values: int) -> Self:
        """
        Set the minimum number of values that can be selected.

        Raises:
            ValueError:
                min_values must be between 1 and 25.
        """
        if min_values < 1 or min_values > 25:
            raise ValueError("Select menu min_values must be between 1 and 25.")
        return set_field_value(self, "min_values", min_values)

    def set_max_values(self, max_values: int) -> Self:
        """
        Set the maximum number of values that can be selected.

        Raises:
            ValueError:
                max_values must be between 1 and 25.
        """
        if max_values < 1 or max_values > 25:
            raise ValueError("Select menu max_values must be between 1 and 25.")
        return set_field_value(self, "max_values", max_values)

    def set_required(self, required: bool) -> Self:
        """
        Set whether this select component is required.
        """
        return set_field_value(self, "required", required)

    def set_disabled(self, disabled: bool) -> Self:
        """
        Set whether this select component is disabled.
        """
        return set_field_value(self, "disabled", disabled)


@dataclass(frozen=True, slots=True)
class AutoPopulatedSelect(SelectMenu):
    """
    Base class for auto populated select manu components.
    """

    default_values: tuple[DefaultValue, ...] | MISSING = MISSING
    """
    List of default values for auto populated select menu components.
    """

    _transforms: ClassVar[dict] = {
        "type": enums.ComponentType,
        "default_values": DefaultValue,
    }

    _default_value_type: ClassVar[Literal["user", "role", "channel"] | None] = (
        None
    )
    """
    Type that will be stamped onto every default value.
    """

    @classmethod
    def new(
        cls,
        *,
        custom_id: str | MISSING = MISSING,
        placeholder: str | MISSING = MISSING,
        default_values: types.TupleOrList[DefaultValue] | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> Self:
        """
        Create a new auto populated select component.

        Raises:
            ValueError:
                Invalid custom ID, placeholder, or values range.
        """
        return (
            cls(custom_id=custom_id)
            .set_placeholder(placeholder)
            .set_min_values(min_values)
            .set_max_values(max_values)
            .set_required(required)
            .set_disabled(disabled)
            .set_default_values(default_values)
        )

    def set_default_values(
        self,
        default_values: types.TupleOrList[DefaultValue] | MISSING = MISSING,
    ) -> Self:
        """
        Set the default values of the select component.
        """
        select = self.clear_default_values()
        if default_values is MISSING:
            return select

        value_type = self._default_value_type
        if value_type is not None:
            default_values = [
                replace(dv, type=value_type) for dv in default_values
            ]
        return select.add_default_values(*default_values)

    def add_default_values(self, *default_values: DefaultValue) -> Self:
        """
        Add default values to the select component.
        """
        select = self
        for value in default_values:
            select = select.add_default_value(value)
        return select

    def add_default_value(self, default_value: DefaultValue) -> Self:
        """
        Add a default value to the select component.
        """
        return add_field_value(self, "default_values", default_value)

    def clear_default_values(self) -> Self:
        """
        Clear all default values from the select component.
        """
        return set_field_value(self, "default_values", MISSING)
