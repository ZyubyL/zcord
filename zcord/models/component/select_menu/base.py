from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Self

from zcord.missing import MISSING
from zcord.models.component.base import Component


@dataclass(frozen=True, slots=True)
class SelectMenu(Component):
    """
    Base class for select menu components.
    Used for type hinting.
    """

    custom_id: str | MISSING = MISSING
    min_values: int | MISSING = MISSING
    max_values: int | MISSING = MISSING
    required: bool | MISSING = MISSING
    disabled: bool | MISSING = MISSING

    def set_custom_id(self, custom_id: str) -> Self:
        """
        Set the custom ID of the string select component.

        Raises:
            ValueError:
                Custom ID must be 100 characters or less.
        """
        if len(custom_id) > 100 or len(custom_id) < 1:
            raise ValueError("Custom ID cannot be longer than 100 characters.")
        return replace(self, custom_id=custom_id)

    def set_min_values(self, min_values: int) -> Self:
        """
        Set the minimum number of values that can be selected.

        Raises:
            ValueError:
                min_values must be between 1 and 25.
        """
        if min_values < 1 or min_values > 25:
            raise ValueError("Select menu min_values must be between 1 and 25.")
        return replace(self, min_values=min_values)

    def set_max_values(self, max_values: int) -> Self:
        """
        Set the maximum number of values that can be selected.

        Raises:
            ValueError:
                max_values must be between 1 and 25.
        """
        if max_values < 1 or max_values > 25:
            raise ValueError("Select menu max_values must be between 1 and 25.")
        return replace(self, max_values=max_values)

    def set_required(self, required: bool) -> Self:
        """
        Set whether this select component is required.
        """
        return replace(self, required=required)

    def set_disabled(self, disabled: bool) -> Self:
        """
        Set whether this select component is disabled.
        """
        return replace(self, disabled=disabled)
