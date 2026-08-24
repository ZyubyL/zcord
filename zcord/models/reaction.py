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
    """

    burst: int
    """
    Count of super reactions.
    """

    normal: int
    """
    Count of normal reactions.
    """


@dataclass(frozen=True, slots=True)
class Reaction(Model):
    """
    Represent a Discord reaction.
    """

    count: int
    """
    Total number of times this emoji has been used to react.
    """

    count_details: ReactionCountDetails
    """
    Reaction count details.
    """

    me: bool
    """
    Whether the bot reacted using this emoji.
    """

    me_burst: bool
    """
    Whether the user super-reacted using this emoji.[^1]

    [^1]: Since bot can't super react, this field should always be `False`(?).
    """

    emoji: Emoji
    """
    Emoji info.
    """

    burst_colors: tuple[int, ...]
    """
    A list of colors used for super reaction.
    """

    _transforms: ClassVar[dict] = {
        "count_details": ReactionCountDetails,
        "emoji": Emoji,
    }
