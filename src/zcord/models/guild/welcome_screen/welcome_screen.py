from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.models.base import Model
from zcord.models.guild.welcome_screen import WelcomeScreenChannel


@dataclass(frozen=True, slots=True)
class WelcomeScreen(Model):
    welcome_channels: tuple[WelcomeScreenChannel, ...]
    """The channels shown in the welcome screen."""

    description: str | None = None
    """The server description shown in the welcome screen."""

    _transforms: ClassVar[dict[str, Any]] = {
        "welcome_channels": WelcomeScreenChannel,
    }
