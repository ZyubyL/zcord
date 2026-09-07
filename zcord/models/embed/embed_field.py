from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedField(Model):
    """
    Contain embed's field info.
    """

    name: str
    """
    The name of the field.
    """

    value: str
    """
    The value of the field.
    """

    inline: bool | MISSING = MISSING
    """
    Whether or not this field should display inline.
    """
