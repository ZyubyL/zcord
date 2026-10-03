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
        r"^<?(?P<animated>a?):(?P<name>\w{2,32}):(?P<id>\d{18,22})>?$"
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

        Raises:
            ValueError:
                The emoji is invalid.

        Examples:
            === "Unicode emoji"
                ```py
                Emoji.new("\N{BROKEN HEART}")  # With emoji name
                Emoji.new("\\U0001f940")  # With unicode codepoint
                ```
            === "Custom emoji"
                ```py
                Emoji.new("<:custom:1234567>") # Static
                Emoji.new("<a:custom_animated:1234567>") # Animated
                ```

        Notes:
            The angled markers (`<>`) can be omitted.
        """
        if match := cls.REGEX.fullmatch(emoji):
            return cls(
                name=match["name"],
                id=Snowflake(match["id"]),
                animated=match["animated"] == "a",
            )

        if cls.is_unicode(emoji):
            return cls(name=emoji)

        raise ValueError(f"Invalid emoji: {emoji!r}")
