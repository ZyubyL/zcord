from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.enums.component import ComponentType
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
    required: bool = True
    disabled: bool = False

    _transforms: ClassVar[dict] = {
        "type": ComponentType,
        "options": SelectOption,
    }


Component._registry[ComponentType.STRING_SELECT] = StringSelect
