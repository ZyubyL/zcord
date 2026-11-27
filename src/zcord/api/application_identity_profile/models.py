from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Media(Model):
    url: str
    """URL of the media asset."""


def _dynamic_field_value(value: Any) -> str | float | Media:
    if isinstance(value, dict):
        return Media._from_payload(value)
    try:
        return float(value)
    except ValueError:
        return str(value)


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


@dataclass(frozen=True, slots=True)
class DynamicField(Model):
    type: enums.DynamicFieldType
    """Field type."""

    name: str
    """Field name."""

    value: str | float | Media
    """Field value.

    This field type is:
        - [`str`][] when `type` is \
        [`enums.DynamicFieldTypes.STRING`][zcord.enums.DynamicFieldTypes.STRING].
        - [`float`][] when `type` is \
        [`enums.DynamicFieldTypes.NUMBER`][zcord.enums.DynamicFieldTypes.NUMBER].
        - [`Media`][] when `type` is \
        [`enums.DynamicFieldTypes.MEDIA`][zcord.enums.DynamicFieldTypes.MEDIA].
    """

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.DynamicFieldType,
        "value": _dynamic_field_value,
    }


@dataclass(frozen=True, slots=True)
class ProfileData(Model):
    primary: PrimaryProfileData | MISSING = MISSING
    """Pre-configured game stat fields."""

    dynamic: tuple[DynamicField, ...] | MISSING = MISSING
    """Custom game stat fields."""

    _transforms: ClassVar[dict[str, Any]] = {
        "primary": PrimaryProfileData,
        "dynamic": DynamicField,
    }


@dataclass(frozen=True, slots=True)
class ApplicationIdentityProfile(Model):
    username: str | None = None
    """The user's username in the external system."""

    metadata: Any | None = None
    """Arbitrary game-defined data."""

    data: ProfileData | None = None
    """The profile data containing game stats."""

    _transforms: ClassVar[dict[str, Any]] = {
        "data": ProfileData,
    }


@dataclass(frozen=True, slots=True)
class ApplicationIdentity(Model):
    user_id: Snowflake
    """The Discord user's ID."""

    provider_type: str
    """The external account provider type."""

    provider_issued_user_id: str
    """The user's ID in the external systemm."""

    provider_id: str | MISSING = MISSING
    """Provider-specific identifier used to disambiguate identities."""

    _transforms: ClassVar[dict[str, Any]] = {
        "user_id": Snowflake,
    }
