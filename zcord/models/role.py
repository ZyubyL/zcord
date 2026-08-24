from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class RoleTags(Model):
    """
    Role tags.
    """

    type null = Literal[True]
    bot_id: Snowflake | MISSING = MISSING
    integration_id: Snowflake | MISSING = MISSING
    premium_subscriber: null | MISSING = MISSING
    subscription_listing_id: Snowflake | MISSING = MISSING
    available_for_purchase: null | MISSING = MISSING
    guild_connections: null | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "bot_id": Snowflake,
        "integration_id": Snowflake,
        "subscription_listing_id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class RoleColors(Model):
    """
    Contain the colors of the role.
    """

    primary_color: int = 0
    """
    The primary color of the role.
    """

    secondary_color: int | None = None
    """
    The secondary color of the role (gradient color).
    """

    tertiary_color: int | None = None
    """
    The tertiary color of the role (holographic style).
    """

    @classmethod
    def default(cls) -> RoleColors:
        """
        Non color role has the default `primary_color` of `0` and `None`
        for other fields.
        """
        return cls()

    @classmethod
    def _from_payload(cls, payload: dict | None) -> RoleColors:
        if payload is None:
            return cls.default()
        return cls(
            primary_color=payload.get("primary_color", 0),
            secondary_color=payload.get("secondary_color"),
            tertiary_color=payload.get("tertiary_color"),
        )


@dataclass(frozen=True, slots=True)
class Role(Model):
    """
    Represent a Discord role.
    """

    id: Snowflake
    """
    The role's ID.
    """

    name: str
    """
    The role's name.
    """

    colors: RoleColors
    """
    The role's colors.
    """

    hoist: bool
    """
    Whether the option for "Display role members separately from online
    members" is enabled.
    """

    position: int
    """
    Position of the role.
    """

    permissions: str
    """
    The role's permissions bit set.
    """

    managed: bool
    """
    Whether the role is managed by an integration.
    """

    mentionable: bool
    """
    Whether the role is mentionable.
    """

    flags: bitfields.RoleFlags
    """
    The role's flags combined as a bitfield.
    """

    tags: RoleTags | MISSING = MISSING
    """
    The tags of the role.
    """

    icon: str | None | MISSING = MISSING
    """
    The role's icon hash.
    """

    unicode_emoji: str | None | MISSING = MISSING
    """
    The role's unicode emoji.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "colors": RoleColors,
        "flags": bitfields.RoleFlags,
        "tags": RoleTags,
    }


@dataclass(frozen=True, slots=True)
class RoleSubscriptionData(Model):
    """
    Contain data of the role subscription purchase or renewal.
    """

    role_subscription_listing_id: Snowflake
    """
    The ID of the SKU and listing that the user is subscribed to.
    """

    tier_name: str
    """
    The name of the tier that the user is subscribed to.
    """

    total_months_subscribed: int
    """
    The cumulative number of months that the user has been subscribed for.
    """

    is_renewal: bool
    """
    Whether this notification is for a renewal rather than a new purchase.
    """

    _transforms: ClassVar[dict] = {
        "role_subscription_listing_id": Snowflake,
    }
