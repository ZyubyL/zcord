from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model
from zcord.models.guild.guild_onboarding.prompt_option import PromptOption
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class OnboardingPrompt(Model):
    id: Snowflake
    """ID of the prompt."""

    type: enums.PromptTypes
    """Type of prompt."""

    options: tuple[PromptOption, ...]
    """Options available within the prompt."""

    title: str
    """Title of the prompt."""

    single_select: bool
    """Whether users are limited to selecting one option for the prompt."""

    required: bool
    """Whether the prompt is required before a user completes the \
    onboarding flow."""

    in_onboarding: bool
    """Whether the prompt is present in the onboarding flow.

    If this is [`False`][], the prompt will only appear in the \
    `Channels & Roles` tab."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.PromptTypes,
        "options": PromptOption,
    }
