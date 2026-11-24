from __future__ import annotations

from dataclasses import dataclass

from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class Media(Model):
    url: str
    """URL of the media asset."""
