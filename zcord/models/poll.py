from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class PollMedia(Model):
    """
    Attributes:
        text:
            The text of the field.

            **Notes**: 300 characters max for question, and 55 max for answer.
        emoji:
            The emoji of the field.
    """

    text: str | MISSING = MISSING
    emoji: Any | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class PollAnswer(Model):
    """
    Attributes:
        answer_id:
            The ID of the answer.
        poll_media:
            The data of the answer.
    """

    poll_media: PollMedia
    answer_id: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "poll_media": PollMedia,
    }

    @classmethod
    def new(
        cls, *, text: str | MISSING = MISSING, emoji: str | MISSING = MISSING
    ) -> PollAnswer:
        """*|classmethod|*

        Create a new poll answer.
        """
        return cls(poll_media=PollMedia(text=text, emoji=emoji))


@dataclass(frozen=True, slots=True)
class PollAnswerCount(Model):
    """
    Represents the number of votes for a single answer.

    Attributes:
        id:
            The ID of the answer.
        count:
            The number of votes for the answer.
        me_voted:
            Whether the bot voted for this answer.
    """

    id: int
    count: int
    me_voted: bool


@dataclass(frozen=True, slots=True)
class PollResults(Model):
    """
    Attributes:
        is_finalized:
            Whether the votes have been precisely counted.
        answer_counts:
            A list of number of votes for each answer.

    Notes:
        https://docs.discord.com/developers/resources/poll#poll-results-object
    """

    is_finalized: bool
    answer_counts: tuple[PollAnswerCount, ...]

    _transforms: ClassVar[dict] = {
        "answer_counts": PollAnswerCount,
    }


@dataclass(frozen=True, slots=True)
class Poll(Model):
    """
    Represents a Discord poll.

    Attributes:
        question:
            The question of the poll.
        answers:
            A list of answers for the poll.
        expiry:
            The time when the poll ends.
        allow_multiselect:
            Whether a user can select multiple answers.
        layout_type:
            The layout type of the poll.
        results:
            The results of the poll.
    """

    question: PollMedia
    answers: tuple[PollAnswer, ...]
    allow_multiselect: bool
    layout_type: int
    expiry: datetime | None = None
    results: PollResults | MISSING = MISSING

    # For creating request. thanks Discord for the inconsistency
    _duration: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "question": PollMedia,
        "expiry": datetime.fromisoformat,
        "answers": PollAnswer,
        "results": PollResults,
    }

    def _check_after(self, payload: dict) -> dict:
        payload["duration"] = self._duration
        return payload

    @classmethod
    def new(
        cls,
        *,
        question: str | MISSING = MISSING,
        answers: tuple[str, ...] | list[str] | MISSING = MISSING,
        duration: int = 24,
        allow_multiselect: bool = False,
    ) -> Poll:
        """*|classmethod|*

        Create a new poll.

        Raises:
            ValueError:
                - Duration must be between 1 and 768 hours.

        Notes:
            `duration` is in hours.
        """

        return cls(
            question=PollMedia(text=question),
            answers=tuple(PollAnswer.new(text=answer) for answer in answers)
            if answers is not MISSING
            else (),
            allow_multiselect=allow_multiselect,
            _duration=duration,
            layout_type=1,
        )

    def set_question(self, question: str) -> Poll:
        """
        Set the question of the poll.
        """
        return replace(self, question=PollMedia(text=question))

    def set_answers(self, answers: tuple[str, ...] | list[str]) -> Poll:
        """
        Set the answers of the poll.
        """
        poll = self
        for answer in answers:
            poll = poll.add_answer(answer)
        return poll

    def add_answer(self, text: str) -> Poll:
        """
        Add an answer to the poll.
        """
        return replace(
            self,
            answers=(
                *self.answers,
                PollAnswer(
                    poll_media=PollMedia(text=text),
                ),
            ),
        )

    def set_duration(self, hours: int) -> Poll:
        """
        Set the duration of the poll.

        Raises:
            ValueError:
                - Duration must be between 1 and 768 hours.
        """
        if hours < 1 or hours > 32 * 24:
            raise ValueError("Duration must be between 1 and 768 hours")
        return replace(self, _duration=hours)

    def set_multiselect(self, allow_multiselect: bool = True) -> Poll:
        """
        Allow multiple answers to be selected.
        """
        return replace(self, allow_multiselect=allow_multiselect)
