from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.application_identity_profile.media import Media
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class PrimaryProfileData(Model):
    season: str | MISSING = MISSING
    """Current game season."""

    rank_name: str | MISSING = MISSING
    """Current rank name."""

    rank_image: Media | MISSING = MISSING
    """Image representing the current rank."""

    highest_rank: str | MISSING = MISSING
    """Highest rank achieved."""

    highest_rank_image: Media | MISSING = MISSING
    """Image representing the highest rank achieved."""

    featured_played_character: str | MISSING = MISSING
    """Name of the featured played character."""

    featured_played_character_image: Media | MISSING = MISSING
    """Image of the featured played character."""

    playtime_hours: float | MISSING = MISSING
    """Total playtime in hours."""

    total_wins: int | MISSING = MISSING
    """Total number of wins."""

    current_period_games: int | MISSING = MISSING
    """Games played in the current period."""

    total_kills: int | MISSING = MISSING
    """Total number of kills."""

    current_period_kills: int | MISSING = MISSING
    """Kills in the current period."""

    total_assists: int | MISSING = MISSING
    """Total number of assists."""

    current_period_assists: int | MISSING = MISSING
    """Assists in the current period."""

    total_deaths: int | MISSING = MISSING
    """Total number of deaths."""

    current_period_deaths: int | MISSING = MISSING
    """Deaths in the current period."""

    _transforms: ClassVar[dict[str, Any]] = {
        "rank_image": Media,
        "highest_rank_image": Media,
        "featured_played_character_image": Media,
    }
