from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, Literal

from zcord.flags import RoleFlags
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

    Attributes:
        primary_color: The primary color of the role.
        secondary_color: The secondary color of the role (gradient color).
        tertiary_color: The tertiary color of the role (holographic style).
    """

    primary_color: int = 0
    secondary_color: int | None = None
    tertiary_color: int | None = None

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

    Attributes:
        id:
            The role's ID.
        name:
            The role's name.
        colors:
            The role's colors.
        hoist:
            Whether the option for "Display role members separately from online
            members" is enabled.
        icon:
            The role's icon hash.
        unicode_emoji:
            The role's unicode emoji.
        position:
            Position of the role.
        permissions:
            The role's permissions bit set.
        managed:
            Whether the role is managed by an integration.
        mentionable:
            Whether the role is mentionable.
        tags:
            The tags of the role.
        flags:
            The role's flags combined as a bitfield.
    """

    id: Snowflake
    name: str
    colors: RoleColors
    hoist: bool
    position: int
    permissions: str
    managed: bool
    mentionable: bool
    flags: RoleFlags
    tags: RoleTags | MISSING = MISSING
    icon: str | None | MISSING = MISSING
    unicode_emoji: str | None | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "colors": RoleColors,
        "flags": RoleFlags,
        "tags": RoleTags,
    }


@dataclass(frozen=True, slots=True)
class RoleSubscriptionData(Model):
    """
    Contain data of the role subscription purchase or renewal.

    Attributes:
        role_subscription_listing_id:
            The ID of the SKU and listing that the user is subscribed to.
        tier_name:
            The name of the tier that the user is subscribed to.
        total_months_subscribed:
            The cumulative number of months that the user has been subscribed \
            for.
        is_renewal:
            Whether this notification is for a renewal rather than a new \
            purchase.
    """

    role_subscription_listing_id: Snowflake
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool

    _transforms: ClassVar[dict] = {
        "role_subscription_listing_id": Snowflake,
    }
