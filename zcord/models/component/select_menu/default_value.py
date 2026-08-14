from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar, Literal

from zcord.errors import ZcordError
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class DefaultValue(ZcordModel):
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

    def _to_payload(self) -> dict:
        if self.id is MISSING or self.type is MISSING:
            raise ZcordError("id and type must be provided")
        return ZcordModel._to_payload(self)

    @classmethod
    def new(
        cls,
        id: Snowflake | MISSING = MISSING,
        type: Literal["user", "role", "channel"] | MISSING = MISSING,
    ) -> DefaultValue:
        return cls(id=id, type=type)

    def set_id(self, id: Snowflake) -> DefaultValue:
        return replace(self, id=id)

    def set_type(
        self, type: Literal["user", "role", "channel"]
    ) -> DefaultValue:
        return replace(self, type=type)
