from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class LobbyMember(Model):
    id: Snowflake
    """The ID of the user."""

    metadata: dict[str, str] | None | MISSING = MISSING
    """Dictionary of string key/value pairs."""

    flags: bitfields.LobbyMemberFlags | MISSING = MISSING
    """Lobby member flags combined as a bitfield."""

    additional_name: str | MISSING = MISSING
    """An additional 1-80 character display name for the member, \
    such as an in-game character name."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "flags": bitfields.LobbyMemberFlags,
    }
