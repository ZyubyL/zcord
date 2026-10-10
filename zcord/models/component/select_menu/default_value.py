from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.missing import MISSING
from zcord.models.base import Model, set_field_value
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class DefaultValue(Model):
    """
    The default value of the select menu.
    """

    id: Snowflake | MISSING = MISSING
    """
    The ID of the user/role/channel.
    """

    type: Literal["user", "role", "channel"] | MISSING = MISSING
    """
    The type of the default value.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }

    def _check_before(self) -> None:
        # Because we set the type in the corresponding Select
        # It won't be MISSING
        if self.id is MISSING:
            raise ValueError("id must be provided")
        if self.type is MISSING:
            raise ValueError("type must be set")

    @classmethod
    def new(
        cls,
        id: Snowflake | MISSING = MISSING,
        type: Literal["user", "role", "channel"] | MISSING = MISSING,
    ) -> DefaultValue:
        return cls(id=id, type=type)

    def set_id(self, id: Snowflake) -> DefaultValue:
        return set_field_value(self, "id", id)
