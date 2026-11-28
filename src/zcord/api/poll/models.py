from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord import enums
from zcord.api.emoji.models import Emoji
from zcord.api.model import Model
from zcord.missing import MISSING


@dataclass(frozen=True, slots=True)
class PollAnswerCount(Model):
    id: int
    """The `answer_id`."""

    count: int
    """The number of votes for this answer."""

    me_voted: bool
    """Whether the current user voted for this answer."""


@dataclass(frozen=True, slots=True)
class PollResults(Model):
    is_finalized: bool
    """Whether the votes have been precisely counted."""

    answer_counts: tuple[PollAnswerCount, ...]
    """The counts for each answer."""

    _transforms: ClassVar[dict[str, Any]] = {
        "answer_counts": PollAnswerCount,
    }


@dataclass(frozen=True, slots=True)
class PollMedia(Model):
    text: str | MISSING = MISSING
    """The text of the field."""

    emoji: Emoji | MISSING = MISSING
    """The emoji of the field."""

    _transforms: ClassVar[dict[str, Any]] = {
        "emoji": Emoji,
    }


@dataclass(frozen=True, slots=True)
class PollAnswer(Model):
    answer_id: int
    """The ID of the answer."""

    poll_media: PollMedia
    """The data of the answer."""

    _transforms: ClassVar[dict[str, Any]] = {
        "poll_media": PollMedia,
    }


@dataclass(frozen=True, slots=True)
class PollCreateRequest(Model):
    question: PollMedia
    """The question of the poll. Only text is supported."""

    answers: tuple[PollAnswer, ...]
    """Each of the answers available in the poll, up to 10."""

    duration: int | MISSING = MISSING
    """Number of hours the poll should be open for, up to 32 days.
    Defaults to 24."""

    allow_multiselect: bool | MISSING = MISSING
    """Whether a user can select multiple answers. Defaults to false."""

    layout_type: enums.LayoutType | MISSING = MISSING
    """The layout type of the poll. Defaults to… `DEFAULT`!"""

    _transforms: ClassVar[dict[str, Any]] = {
        "question": PollMedia,
        "answers": PollAnswer,
        "layout_type": enums.LayoutType,
    }


@dataclass(frozen=True, slots=True)
class Poll(Model):
    question: PollMedia
    """The question of the poll. Only text is supported."""

    answers: tuple[PollAnswer, ...]
    """Each of the answers available in the poll."""

    allow_multiselect: bool
    """Whether a user can select multiple answers."""

    layout_type: enums.LayoutType
    """The layout type of the poll."""

    expiry: datetime | None = None
    """The time when the poll ends."""

    results: PollResults | MISSING = MISSING
    """The results of the poll."""

    _transforms: ClassVar[dict[str, Any]] = {
        "question": PollMedia,
        "answers": PollAnswer,
        "expiry": datetime.fromisoformat,
        "layout_type": enums.LayoutType,
        "results": PollResults,
    }
