from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar

from zcord import enums, errors
from zcord.missing import MISSING
from zcord.models.base import add_field_value, set_field_value
from zcord.models.component.base import Component
from zcord.models.component.button import Button
from zcord.models.component.select_menu.base import SelectMenu

if TYPE_CHECKING:
    from zcord import types


@dataclass(frozen=True, slots=True)
class ActionRow(Component):
    """
    Represent an action row that holds max to 5 buttons or a select menu.
    """

    type: enums.ComponentType = enums.ComponentType.ACTION_ROW

    components: tuple[Button | SelectMenu, ...] | MISSING = MISSING
    """
    A list of components inside the action row.
    """

    _transforms: ClassVar[dict] = {
        "type": enums.ComponentType,
        "components": Component,
    }

    @classmethod
    def new(
        cls,
        components: types.TupleOrList[Button] | SelectMenu | MISSING = MISSING,
    ) -> ActionRow:
        """
        Create a new action row component.
        """
        if components is MISSING:
            return cls()

        row = cls()
        if isinstance(components, SelectMenu):
            row = row.set_select(components)
        else:
            row = row.set_buttons(*components)
        return row

    def set_buttons(self, *buttons: Button) -> ActionRow:
        """
        Set the buttons of the action row.

        Raises:
            errors.ZcordError:
                Cannot add more components to this action row.
        """
        row = self
        for button in buttons:
            row = row.add_button(button)
        return row

    def add_button(self, button: Button) -> ActionRow:
        """
        Add a button to the action row.

        Raises:
            errors.ZcordError:
                Cannot add more components to this action row.
        """
        if self.components is MISSING or not self.components:
            return set_field_value(self, "components", (button,))
        if isinstance(self.components[0], SelectMenu) or (
            isinstance(self.components[0], Button) and len(self.components) >= 5
        ):
            raise errors.ZcordError(
                "Cannot add more components to this action row"
            )
        return add_field_value(self, "components", button)

    def set_select(self, select: SelectMenu) -> ActionRow:
        """
        Set the select menu of the action row.

        Raises:
            TypeError:
                A bare [`SelectMenu`][] or [`AutoPopulatedSelect`][] \
                has been passed.

        Notes:
            This will replace any existing select menu or buttons.
        """
        # Since the bare SelectMenu/AutoPopulatedSelect doesn't have
        # the type field, we can check if it exist to detect if it is bare class
        if not hasattr(select, "type"):
            raise TypeError("Cannot add bare SelectMenu/AutoPopulatedSelect.")
        return set_field_value(self, "components", (select,))


Component._registry[enums.ComponentType.ACTION_ROW] = ActionRow
