from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import cdn
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class SoundboardSound(Model):
    name: str
    """The name of this sound."""

    sound_id: Snowflake
    """the ID of this sound."""

    volume: float
    """The volume of this sound, from 0 to 1"""

    available: bool
    """Whether this sound can be used, \
    may be `False` due to loss of Server Boosts."""

    emoji_id: Snowflake | None = None
    """The ID of this sound's custom emoji."""

    emoji_name: str | None = None
    """The unicode character of this sound's standard emoji."""

    guild_id: Snowflake | MISSING = MISSING
    """The ID of the guild this sound is in."""

    user: User | MISSING = MISSING
    """The user who created this sound."""

    _transforms: ClassVar[dict[str, Any]] = {
        "sound_id": Snowflake,
        "emoji_id": Snowflake,
        "guild_id": Snowflake,
        "user": User,
    }

    @property
    def url(self) -> str:
        return cdn.sound_file(sound_id=str(self.sound_id))
