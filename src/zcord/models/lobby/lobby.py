from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.channel.channel import Channel
from zcord.models.lobby.lobby_member import LobbyMember
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Lobby(Model):
    id: Snowflake
    """The ID of this channel."""

    application_id: Snowflake
    """Application that created the lobby."""

    members: tuple[LobbyMember, ...]
    """Members of the lobby."""

    metadata: dict[str, str] | None = None
    """Dictionary of string key/value pairs."""

    linked_channel: Channel | MISSING = MISSING
    """The guild channel linked to the lobby."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "application_id": Snowflake,
        "members": LobbyMember,
        "linked_channel": Channel,
    }
