from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ForumTag(Model):
    id: Snowflake
    """The ID of the tag."""

    name: str
    """The name of the tag."""

    moderated: bool
    """Whether this tag can only be added to or removed from threads \
    by a member of with the `MANAGE_THREADS` permission."""

    emoji_id: Snowflake | None = None
    """The ID of a guild's custom emoji.

    Notes:
        At least this field or `emoji_name` field need to have a value.
    """

    emoji_name: str | None = None
    """The unicode character of the emoji.

    Notes:
        At least this field or `emoji_id` field need to have a value.
    """

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "emoji_id": Snowflake,
    }
