from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.base import Model
from zcord.models.guild.guild_onboarding.onboarding_prompt import (
    OnboardingPrompt,
)
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class GuildOnboarding(Model):
    guild_id: Snowflake
    """ID of the guild this onboarding is part of."""

    prompts: tuple[OnboardingPrompt, ...]
    """Prompts shown during onboarding and in customize community."""

    default_channel_ids: tuple[Snowflake, ...]
    """Channel IDs that members get opted into automatically."""

    enabled: bool
    """Whether onboarding is enabled in the guild."""

    mode: enums.OnboardingMode
    """Current mode of onboarding."""

    _transforms: ClassVar[dict[str, Any]] = {
        "guild_id": Snowflake,
        "prompts": OnboardingPrompt,
        "default_channel_ids": Snowflake,
        "mode": enums.OnboardingMode,
    }
