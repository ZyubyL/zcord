from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord import enums, types
from zcord.missing import MISSING
from zcord.models.base import add_field_value, set_field_value
from zcord.models.component.base import Component
from zcord.models.component.select_menu.base import SelectMenu
from zcord.models.component.select_menu.default_value import DefaultValue


@dataclass(frozen=True, slots=True)
class MentionableSelect(SelectMenu):
    """A mentionable select menu component"""

    type: enums.ComponentType = enums.ComponentType.MENTIONABLE_SELECT

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
        default_values: types.TupleOrList[DefaultValue] | MISSING = MISSING,
        min_values: int = 1,
        max_values: int = 1,
        required: bool = True,
        disabled: bool = False,
    ) -> MentionableSelect:
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
    ) -> MentionableSelect:
        """
        Set the placeholder of the mentionable select component.

        Raises:
            ValueError:
                Placeholder cannot be longer than 150 characters.
        """
        if placeholder is not MISSING and len(placeholder) > 150:
            raise ValueError(
                "Placeholder cannot be longer than 150 characters."
            )
        return set_field_value(self, "placeholder", placeholder)

    def set_default_values(
        self,
        default_values: types.TupleOrList[DefaultValue] | MISSING = MISSING,
    ) -> MentionableSelect:
        """
        Set the default values of the mentionable select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        select = self.clear_default_values()
        if default_values is MISSING:
            return select

        default_values = [replace(dv, type="role") for dv in default_values]
        return select.add_default_values(*default_values)

    def add_default_values(
        self, *default_values: DefaultValue
    ) -> MentionableSelect:
        """
        Add default values to the mentionable select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        select = self
        for value in default_values:
            select = select.add_default_value(value)
        return select

    def add_default_value(
        self, default_value: DefaultValue
    ) -> MentionableSelect:
        """
        Add a default value to the mentionable select component.

        Raises:
            ValueError:
                Default values cannot have more than 25 options.
        """
        return add_field_value(self, "default_values", default_value)

    def clear_default_values(self) -> MentionableSelect:
        """
        Clear all default values from the mentionable select component.
        """
        return set_field_value(self, "default_values", MISSING)


Component._registry[enums.ComponentType.MENTIONABLE_SELECT] = MentionableSelect
