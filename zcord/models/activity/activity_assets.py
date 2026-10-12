from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ActivityAssets(Model):
    """Contain images for the presence and their hover texts."""

    large_image: str | MISSING = MISSING
    """The large image display in the activity card."""

    large_text: str | MISSING = MISSING
    """The text displayed when hovering over the large image of the activity."""

    large_url: str | MISSING = MISSING
    """The URL that is opened when clicking on the large image."""

    small_image: str | MISSING = MISSING
    """The small image display in the activity card."""

    small_text: str | MISSING = MISSING
    """The text displayed when hovering over the small image of the activity."""

    small_url: str | MISSING = MISSING
    """The URL that is opened when clicking on the small image."""

    invite_cover_image: str | MISSING = MISSING
    """The asset that will be displayed as a banner on a game invite."""

    # TODO: Activity asset image
