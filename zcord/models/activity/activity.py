from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord import bitfields, enums
from zcord.missing import MISSING
from zcord.models.activity.activity_assets import ActivityAssets
from zcord.models.activity.activity_button import ActivityButton
from zcord.models.activity.activity_emoji import ActivityEmoji
from zcord.models.activity.activity_party import ActivityParty
from zcord.models.activity.activity_secrets import ActivitySecrets
from zcord.models.activity.activity_timestamp import ActivityTimestamp
from zcord.models.base import Model, set_field_value
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Activity(Model):
    """Represent and activity shown in a [`Presence`][]."""

    created_at: datetime | MISSING = MISSING
    """Unix timestamp (in milliseconds) of when the activity was added to \
    the user's session.
    """

    timestamps: ActivityTimestamp | MISSING = MISSING
    """Unix timestamps for start/or end of the game."""

    application_id: Snowflake | MISSING = MISSING
    """Application ID of the game."""

    status_display_type: enums.StatusDisplayType | MISSING = MISSING
    """Controls which field is displayed in the user's status text \
    in the member list.
    """

    details: str | None | MISSING = MISSING
    """What the player is currently doing."""

    details_url: str | None | MISSING = MISSING
    """URL that is linked when clicking on the details text."""

    state_url: str | None | MISSING = MISSING
    """URL that is linked when clicking on the state text."""

    emoji: ActivityEmoji | None | MISSING = MISSING
    """Emoji used for a custom status."""

    party: ActivityParty | MISSING = MISSING
    """Information for the current party of the player"""

    assets: ActivityAssets | MISSING = MISSING
    """Images for the presence and their text hover."""

    secrets: ActivitySecrets | MISSING = MISSING
    """Secrets for Rich Presence joining and spectating."""

    instance: bool | MISSING = MISSING
    """Whether the activity is an instanced game session."""

    flags: bitfields.ActivityFlags | MISSING = MISSING
    """Activity flags"""

    buttons: tuple[ActivityButton, ...] | MISSING = MISSING

    name: str | MISSING = MISSING
    """The activity name."""

    type: enums.ActivityType | MISSING = MISSING
    """The activity's [`type`][zcord.enums.ActivityType]."""

    url: str | MISSING = MISSING
    """The stream URL. Only validated when `type` is \
    [`STREAMING`][zcord.enums.ActivityType.STREAMING].
    """

    state: str | MISSING = MISSING
    """The player's current party status, or text for a custom status."""

    _transforms: ClassVar[dict] = {
        "created_at": datetime.fromisoformat,
        "timestamps": ActivityTimestamp,
        "application_id": Snowflake,
        "status_display_type": enums.StatusDisplayType,
        "emoji": ActivityEmoji,
        "party": ActivityParty,
        "assets": ActivityAssets,
        "secrets": ActivitySecrets,
        "flags": bitfields.ActivityFlags,
        "buttons": ActivityButton,
        "type": enums.ActivityType,
    }

    @classmethod
    def new(
        cls,
        *,
        name: str | MISSING = MISSING,
        type: enums.ActivityType | MISSING = MISSING,
        url: str | MISSING = MISSING,
        state: str | MISSING = MISSING,
    ) -> Activity:
        """Create a new activity."""
        return cls().set_name(name).set_type(type).set_url(url).set_state(state)

    def set_name(self, name: str | MISSING = MISSING) -> Activity:
        """Set the activity name.

        Notes:
            Won't display when use with \
            [`enums.ActivityType.CUSTOM`][zcord.enums.ActivityType.CUSTOM]
        """
        return set_field_value(self, "name", name)

    def set_type(
        self, type: enums.ActivityType | MISSING = MISSING
    ) -> Activity:
        """Set the activity type."""
        return set_field_value(self, "type", type)

    def set_url(self, url: str | MISSING = MISSING) -> Activity:
        """Set the activity URL."""
        return set_field_value(self, "url", url)

    def set_state(self, state: str | MISSING = MISSING) -> Activity:
        """Set the activity status."""
        return set_field_value(self, "state", state)
