from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Literal

import regex

from zcord.cdn import CDN
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    import re


@dataclass(frozen=True, slots=True)
class Emoji(Model):
    """
    Represent a Discord emoji.
    """

    id: Snowflake | None = None
    """
    The ID of the emoji.
    """

    name: str | None = None
    """
    The name of the emoji.
    """

    roles: tuple[Snowflake, ...] | MISSING = MISSING
    """
    A list of role IDs that the emoji is restricted to.
    """

    user: User | MISSING = MISSING
    """
    The user who created the emoji.
    """

    require_colons: bool | MISSING = MISSING
    """
    Whether the emoji requires colons to be used.
    """

    managed: bool | MISSING = MISSING
    """
    Whether the emoji is managed.
    """

    animated: bool | MISSING = MISSING
    """
    Whether the emoji is animated.
    """

    available: bool | MISSING = MISSING
    """
    Whether the emoji is available.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "roles": Snowflake,
        "user": User,
    }

    REGEX: ClassVar[re.Pattern] = regex.compile(
        r"^<?(?:(?P<animated>a):)?(?P<name>[^:]+):(?P<id>\d+)>?$"
    )

    _EMOJI_REGEX: ClassVar[re.Pattern] = regex.compile(r"\X")

    @classmethod
    def is_unicode(cls, emoji: str) -> bool:
        """
        Check if the emoji is a valid Unicode emoji.
        """
        clusters = cls._EMOJI_REGEX.findall(emoji)
        return (
            len(clusters) == 1
            and regex.search(r"\p{Emoji}", clusters[0]) is not None
        )

    def url(
        self,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp", "gif"] | None = None,
    ) -> str | None:
        """
        The URL of the emoji.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if self.id is None:
            return None
        return CDN.emoji(
            hash=str(self.id),
            size=size,
            format=format,
        )

    @classmethod
    def new(cls, emoji: str) -> Emoji:
        """
        Create a new emoji object.

        Examples:
            ```py
            # 1. Unicode emoji
            Emoji.new("\N{ROLLING ON THE FLOOR LAUGHING}")

            # 2. Custom static emoji
            Emoji.new("<:custom:1234567>")
            # 3. Custom animated emoji
            Emoji.new("<a:custom:1234567>")

            # NOTE: The '<>' can be omitted
            Emoji.new(":custom:1234567")

            ```
        """
        if match := cls.REGEX.fullmatch(emoji):
            return cls(
                name=match["name"],
                id=Snowflake(match["id"]),
                animated=match["animated"] is not None,
            )

        if cls.is_unicode(emoji):
            return cls(name=emoji)

        raise ValueError(f"Invalid emoji: {emoji!r}")
