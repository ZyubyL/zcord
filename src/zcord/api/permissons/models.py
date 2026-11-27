from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields
from zcord.api.model import Model
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


def _null_flag(value: Any) -> bool | MISSING:
    # Discord is very funny on this one and treat null as true
    if value is None:
        return True
    if value is MISSING:
        return MISSING
    return bool(value)


@dataclass(frozen=True, slots=True)
class RoleTags(Model):
    bot_id: Snowflake | MISSING = MISSING
    """The ID of the bot this role belongs to."""

    integration_id: Snowflake | MISSING = MISSING
    """The ID of the integration this role belongs to."""

    premium_subscriber: bool | MISSING = MISSING
    """Whether this the guild's Booster role."""

    subscription_listing_id: Snowflake | MISSING = MISSING
    """The ID of this role's subscription SKU and listing."""

    available_for_purchase: bool | MISSING = MISSING
    """Whether this role is available for purchase."""

    guild_connections: bool | MISSING = MISSING
    """Whether this role is a guild's linked role."""

    _transforms: ClassVar[dict[str, Any]] = {
        "bot_id": Snowflake,
        "integration_id": Snowflake,
        "subscription_listing_id": Snowflake,
        "premium_subscriber": _null_flag,
        "available_for_purchase": _null_flag,
        "guild_connections": _null_flag,
    }


@dataclass(frozen=True, slots=True)
class RoleColors(Model):
    primary_color: int = 0
    """The primary color of the role."""

    secondary_color: int | None = None
    """The secondary color of the role.

    This will make the role a gradient between the other provided colors.
    """

    tertiary_color: int | None = None
    """The tertiary color of the role.

    This will turn the gradient into a holographic style.
    """

    @classmethod
    def from_payload(
        cls, payload: dict[str, Any] | None | MISSING
    ) -> RoleColors | MISSING:
        if payload is MISSING:
            return MISSING
        if payload is None:
            return cls()
        return cls(
            primary_color=payload.get("primary_color", 0),
            secondary_color=payload.get("secondary_color"),
            tertiary_color=payload.get("tertiary_color"),
        )


@dataclass(frozen=True, slots=True)
class Role(Model):
    id: Snowflake
    """Role ID."""

    name: str
    """Role name."""

    colors: RoleColors
    """The role's colors."""

    hoist: bool
    """If this role is pinned in the user listing."""

    position: int
    """Position of this role."""

    permissions: str
    """Permission bit set."""

    managed: bool
    """Whether this role is managed by an integration."""

    mentionable: bool
    """Whether this role is mentionable."""

    flags: bitfields.RoleFlags

    icon: str | None | MISSING = MISSING
    """Role icon hash."""

    unicode_emoji: str | None | MISSING = MISSING
    """Role unicode emoji."""

    tags: RoleTags | MISSING = MISSING
    """The tags this role has."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "colors": RoleColors.from_payload,
        "flags": bitfields.RoleFlags,
        "tags": RoleTags,
    }
