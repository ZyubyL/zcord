from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, overload

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class Component(Model):
    """
    Generic component model.
    """

    _registry: ClassVar[dict[enums.ComponentType, type[Component]]] = {}

    id: str | MISSING = MISSING

    @classmethod
    @overload
    def _from_payload(cls, payload: dict) -> Component: ...
    @classmethod
    @overload
    def _from_payload(cls, payload: MISSING) -> MISSING: ...
    @classmethod
    def _from_payload(
        cls, payload: dict | MISSING = MISSING
    ) -> Component | MISSING:
        if payload is MISSING:
            return MISSING
        component_cls = cls._registry.get(
            enums.ComponentType(payload["type"]), cls
        )
        return Model._from_payload.__func__(
            component_cls,
            payload,
        )

    def _check_before(self) -> None:
        if hasattr(self, "custom_id") and self.custom_id is MISSING:
            raise ValueError("custom_id must be set")
