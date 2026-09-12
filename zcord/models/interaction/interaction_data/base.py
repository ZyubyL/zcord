from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from zcord.models.base import Model

if TYPE_CHECKING:
    from zcord import enums


class InteractionData(Model):
    """
    Base class for interaction data payloads.
    """

    _registry: ClassVar[dict[enums.InteractionType, type[InteractionData]]] = {}
