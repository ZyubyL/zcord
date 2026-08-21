from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord.models.base import Model
from zcord.models.emoji import Emoji


@dataclass(frozen=True, slots=True)
class ReactionCountDetails(Model):
    """
    Contain a breakdown of normal and super reaction counts for the associated \
    emoji.

    Attributes:
        burst:
            Count of super reactions.
        normal:
            Count of normal reactions.
    """

    burst: int
    normal: int


@dataclass(frozen=True, slots=True)
class Reaction(Model):
    """
    Represent a Discord reaction.

    Attributes:
        count:
            Total number of times this emoji has been used to react.
        count_details:
            Reaction count details.
        me:
            Whether the bot reacted using this emoji.
        me_burst:
            Whether the bot super-reacted using this emoji.
        emoji:
            Emoji info.
        burst_colors:
            A list of colors used for super reaction.
    """

    count: int
    count_details: ReactionCountDetails
    me: bool
    me_burst: bool
    emoji: Emoji
    burst_colors: tuple[int, ...]

    _transforms: ClassVar[dict] = {
        "count_details": ReactionCountDetails,
        "emoji": Emoji,
    }
