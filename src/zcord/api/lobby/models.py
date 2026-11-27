from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields
from zcord.api.channel.models import Channel
from zcord.api.model import Model
from zcord.missing import MISSING
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
