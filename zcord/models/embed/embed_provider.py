from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedProvider(Model):
    """
    Contain embed's provider info.
    """

    name: str | MISSING = MISSING
    """
    Name of the provider.
    """

    url: str | MISSING = MISSING
    """
    URL of the provider.
    """
