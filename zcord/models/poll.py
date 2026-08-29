from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.emoji import Emoji


@dataclass(frozen=True, slots=True)
class PollMedia(Model):
    """
    Generic poll media data.
    """

    text: str | MISSING = MISSING
    """
    The text of the field.

    **Notes**: 300 characters max for question, and 55 max for answer.
    """

    emoji: Emoji | MISSING = MISSING
    """
    The emoji of the field.
    """

    _transforms: ClassVar[dict] = {
        "emoji": Emoji,
    }

    _is_question: bool = False

    def _check_before(self) -> None:
        if self.text is MISSING or not self.text:
            raise ValueError("text is required")
        if self._is_question and len(self.text) > 300:
            raise ValueError("question must be 300 characters or less")
        if len(self.text) > 55:
            raise ValueError("answer must be 55 characters or less")


@dataclass(frozen=True, slots=True)
class PollAnswer(Model):
    """
    Contain info about a poll answer.
    """

    poll_media: PollMedia
    """
    The data of the answer.
    """

    answer_id: int | MISSING = MISSING
    """
    The ID of the answer.
    """

    _transforms: ClassVar[dict] = {
        "poll_media": PollMedia,
    }

    @classmethod
    def new(
        cls,
        *,
        text: str | MISSING = MISSING,
        emoji: Emoji | str | MISSING = MISSING,
    ) -> PollAnswer:
        """
        Create a new poll answer.
        """
        return cls(
            poll_media=PollMedia(
                text=text,
                emoji=emoji
                if isinstance(emoji, Emoji)
                else Emoji.new(emoji)
                if emoji is not MISSING
                else MISSING,
            )
        )


@dataclass(frozen=True, slots=True)
class PollAnswerCount(Model):
    """
    Contain info about the poll answer vote count.
    """

    id: int
    """
    The ID of the answer.
    """

    count: int
    """
    The number of votes for the answer.
    """

    me_voted: bool
    """
    Whether the bot voted for this answer.
    """


@dataclass(frozen=True, slots=True)
class PollResults(Model):
    """
    Contain info about the poll results.
    """

    is_finalized: bool
    """
    Whether the votes have been precisely counted.
    """

    answer_counts: tuple[PollAnswerCount, ...]
    """
    A list of number of votes for each answer.
    """

    _transforms: ClassVar[dict] = {
        "answer_counts": PollAnswerCount,
    }


@dataclass(frozen=True, slots=True)
class Poll(Model):
    """
    Represent a Discord poll.
    """

    question: PollMedia | MISSING = MISSING
    """
    The question of the poll.
    """

    answers: tuple[PollAnswer, ...] | MISSING = MISSING
    """
    A list of answers for the poll.
    """

    allow_multiselect: bool = False
    """
    Whether a user can select multiple answers.
    """

    layout_type: int = 1
    """
    The layout type of the poll.[^1]

    [^1]: Discord only supports layout type `1` for now.
    """

    expiry: datetime | None = None
    """
    The time when the poll ends.
    """

    results: PollResults | MISSING = MISSING
    """
    The results of the poll.
    """

    # For creating request. thanks Discord for the inconsistency
    _duration: int | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "question": PollMedia,
        "expiry": datetime.fromisoformat,
        "answers": PollAnswer,
        "results": PollResults,
    }

    def _check_before(self) -> None:
        if self.question is MISSING:
            raise ValueError("question is required")
        if not self.answers or self.answers is MISSING:
            raise ValueError("answers are required")

    def _check_after(self, payload: dict) -> dict:
        payload["duration"] = self._duration
        return payload

    @classmethod
    def new(
        cls,
        *,
        question: str | MISSING = MISSING,
        answers: tuple[PollAnswer, ...] | list[PollAnswer] | MISSING = MISSING,
        duration: int = 24,
        allow_multiselect: bool = False,
    ) -> Poll:
        """
        Create a new poll.

        Raises:
            ValueError:
                Duration must be between 1 and 768 hours.

        Notes:
            `duration` is in hours.
        """

        return (
            cls()
            .set_question(question)
            .set_answers(answers)
            .set_multiselect(allow_multiselect)
            .set_duration(duration)
        )

    def set_question(self, question: str | MISSING = MISSING) -> Poll:
        """
        Set the question of the poll.
        """
        return replace(
            self, question=PollMedia(text=question, _is_question=True)
        )

    def set_answers(
        self,
        answers: tuple[PollAnswer, ...] | list[PollAnswer] | MISSING = MISSING,
    ) -> Poll:
        """
        Set the answers of the poll.
        """
        poll = self.clear_answers()
        if answers is not MISSING:
            for answer in answers:
                poll = poll.add_answer(answer=answer)
        return poll

    def add_answer(
        self,
        *,
        text: str | MISSING = MISSING,
        emoji: Emoji | str | MISSING = MISSING,
        answer: PollAnswer | MISSING = MISSING,
    ) -> Poll:
        """
        Add an answer to the poll.

        Parameters:
            text:
                The text of the answer.
            emoji:
                The emoji of the answer.
            answer:
                The answer to add.

        Notes:
            If `answer` is provided, `text` and `emoji` are ignored.
        """
        if answer is MISSING:
            answer = PollAnswer(
                poll_media=PollMedia(
                    text=text,
                    emoji=emoji
                    if isinstance(emoji, Emoji)
                    else Emoji.new(emoji)
                    if emoji is not MISSING
                    else MISSING,
                )
            )
        return replace(
            self,
            answers=(*self.answers, answer)
            if self.answers is not MISSING
            else (answer,),
        )

    def clear_answers(self) -> Poll:
        """
        Clear all answers from the poll.
        """
        return replace(self, answers=MISSING)

    def set_duration(self, hours: int = 24) -> Poll:
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
