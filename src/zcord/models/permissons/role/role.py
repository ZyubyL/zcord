from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.permissons.role.role_colors import RoleColors
from zcord.models.permissons.role.role_tags import RoleTags
from zcord.snowflake import Snowflake


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
