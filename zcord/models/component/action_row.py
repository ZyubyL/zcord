from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord.enums.component import ComponentType
from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.component.base import Component
from zcord.models.component.button import Button
from zcord.models.component.select_menu.base import SelectMenu


@dataclass(frozen=True, slots=True)
class ActionRow(Component):
    """
    Represent an action row that holds max to 5 buttons or a select menu.
    """

    type: ComponentType = ComponentType.ACTION_ROW

    components: tuple[Button | SelectMenu, ...] | MISSING = MISSING
    """
    A list of components inside the action row.
    """

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "components": Component,
    }

    @classmethod
    def new(
        cls,
        components: list[Button]
        | tuple[Button, ...]
        | SelectMenu
        | MISSING = MISSING,
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
            row = row.set_buttons(components)
        return row

    def set_buttons(
        self, buttons: tuple[Button, ...] | list[Button]
    ) -> ActionRow:
        """
        Set the buttons of the action row.

        Raises:
            ZcordError:
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
            ZcordError:
                Cannot add more components to this action row.
        """
        if self.components is MISSING or not self.components:
            return replace(self, components=(button,))
        if isinstance(self.components[0], SelectMenu) or (
            isinstance(self.components[0], Button) and len(self.components) >= 5
        ):
            raise ZcordError("Cannot add more components to this action row")
        return replace(self, components=(*self.components, button))

    def set_select(self, select: SelectMenu) -> ActionRow:
        """
        Set the select menu of the action row.

        Notes:
            This will replace any existing select menu or buttons.
        """
        return replace(self, components=(select,))


Component._registry[ComponentType.ACTION_ROW] = ActionRow
