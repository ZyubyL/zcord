from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar, Literal

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class DefaultValue(Model):
    """
    The default value of the select menu.

    Attributes:
        id:
            The ID of the user/role/channel.
        type:
            The type of the default value.
    """

    id: Snowflake | MISSING = MISSING
    type: Literal["user", "role", "channel"] | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }

    def _check_before(self) -> None:
        # Because we set the type in the corresponding Select
        # It won't be MISSING
        if self.id is MISSING:
            raise ValueError("id must be provided")

    @classmethod
    def new(
        cls,
        id: Snowflake | MISSING = MISSING,
    ) -> DefaultValue:
        return cls(id=id)

    def set_id(self, id: Snowflake) -> DefaultValue:
        return replace(self, id=id)
