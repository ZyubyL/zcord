from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.api.guild.models import Guild
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildTemplate(Model):
    code: str
    """The template code (unique ID)."""

    name: str
    """Template name."""

    usage_count: int
    """Number of times this template has been used."""

    creator_id: Snowflake
    """The ID of the user who created the template."""

    creator: User
    """The user who created the template."""

    created_at: datetime
    """When this template was created."""

    updated_at: datetime
    """When this template was last synced to the source guild."""

    source_guild_id: Snowflake
    """The ID of the guild this template is based on."""

    serialized_source_guild: Guild
    """The guild snapshot this template contains.

    Placeholder IDs are given as integers."""

    is_dirty: bool | None = None
    """Whether the template has unsynced changes."""

    description: str | None = None
    """The description for the template."""

    _transforms: ClassVar[dict[str, Any]] = {
        "creator_id": Snowflake,
        "creator": User,
        "created_at": datetime.fromisoformat,
        "updated_at": datetime.fromisoformat,
        "source_guild_id": Snowflake,
        "serialized_source_guild": Guild,
    }
