from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, overload

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

if TYPE_CHECKING:
    from datetime import datetime


@dataclass(frozen=True, slots=True)
class Activity(Model):
    """Represent an activity."""

    created_at: int | MISSING = MISSING
    """Unix time (in milliseconds) for when the activity session started.

    Notes:
        This is what Discord sends to the client.
        Use `created_time` to get this value in \
        [`datetime`][datetime.datetime] format.
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
    """Activity flags."""

    buttons: tuple[ActivityButton, ...] | MISSING = MISSING
    """The buttons shown under the activity.

    Notes:
        Discord doesn't exposes button URL to bots. They only send a list \
        of button labels.
        This is wrapped as a list of [`ActivityButton`][] for compliance with \
        Discord docs.
    """

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

    @property
    def created_time(self) -> datetime | MISSING:
        """The time when this activity was added to the user's session."""
        return ActivityTimestamp._to_datetime(self.created_at)

    @classmethod
    @overload
    def _from_payload(cls, payload: dict) -> Activity: ...
    @classmethod
    @overload
    def _from_payload(cls, payload: MISSING) -> MISSING: ...
    @classmethod
    def _from_payload(cls, payload: dict | MISSING) -> Activity | MISSING:
        if payload is MISSING:
            return MISSING
        # The gateway sends buttons as an array of button labels.
        # But they require us to send them correct structure.
        # Thank you Discord.
        buttons = payload.get("buttons")
        if isinstance(buttons, list):
            payload = {
                **payload,
                "buttons": [
                    {"label": b} if isinstance(b, str) else b for b in buttons
                ],
            }
        return Model._from_payload.__func__(cls, payload)

    def _check_before(self) -> None:
        """
        Raises:
            ValueError:
                `name` and `type` are required before sending.
        """
        if self.name is MISSING:
            raise ValueError("activity name is required")
        if self.type is MISSING:
            raise ValueError("activity type is required")

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
