from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.models.base import Model


@dataclass
class _SessionStartLimit(Model):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


@dataclass
class _GetGatewayBotResponse(Model):
    url: str
    shards: int
    session_start_limit: _SessionStartLimit

    _transforms: ClassVar[dict] = {"session_start_limit": _SessionStartLimit}
