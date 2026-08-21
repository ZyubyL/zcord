from __future__ import annotations

from typing import ClassVar

from zcord.enums.component import ComponentType
from zcord.missing import MISSING
from zcord.models.base import Model, from_payload


class Component(Model):
    """
    Generic component model.
    """

    _registry: ClassVar[dict[ComponentType, type[Component]]] = {}

    type: ComponentType
    id: str | MISSING = MISSING

    @classmethod
    def _from_payload(
        cls, payload: dict | MISSING = MISSING
    ) -> Component | MISSING:
        if payload is MISSING:
            return MISSING
        component_cls = cls._registry.get(ComponentType(payload["type"]), cls)
        return from_payload(
            component_cls,
            payload,
            **getattr(component_cls, "_transforms", {}),
        )
