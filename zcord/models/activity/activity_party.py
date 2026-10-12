from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple, overload

from zcord.missing import MISSING
from zcord.models.base import Model


class ActivityPartySize(NamedTuple):
    current_size: int
    max_size: int


@dataclass(frozen=True, slots=True)
class ActivityParty(Model):
    """Contain information for the current party of the player."""

    id: str | MISSING = MISSING
    """The ID of the party."""

    size: ActivityPartySize | MISSING = MISSING
    """The party current and maximum size."""

    @overload
    @classmethod
    def _from_payload(cls, payload: dict) -> ActivityParty: ...
    @overload
    @classmethod
    def _from_payload(cls, payload: MISSING) -> MISSING: ...
    @classmethod
    def _from_payload(cls, payload=MISSING) -> ActivityParty | MISSING:
        if payload is MISSING:
            return MISSING
        size = payload.get("size")
        if isinstance(size, (tuple, list)):
            payload = {**payload, "size": ActivityPartySize(*size)}

        return Model()._from_payload.__func__(cls, payload)
