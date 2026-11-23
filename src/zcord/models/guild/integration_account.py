from __future__ import annotations

from dataclasses import dataclass

from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class IntegrationAccount(Model):
    id: str
    """ID of the account."""

    name: str
    """Name of the account."""
