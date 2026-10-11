from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar, overload

from zcord import bitfields, enums, types
from zcord.missing import MISSING
from zcord.models.base import Model, add_field_value, set_field_value
from zcord.models.emoji import Emoji
from zcord.models.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class ActivityTimestamp(Model):
    start: datetime | MISSING = MISSING
    end: datetime | MISSING = MISSING


@dataclass(frozen=True, slots=True)
class ActivityButton(Model):
    label: str
    url: str


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

    emoji: Emoji | None | MISSING = MISSING
    """Emoji used for a custom status."""

    party: Any | MISSING = MISSING
    """Information for the current party of the player"""

    assets: Any | MISSING = MISSING
    """Images for the presence and their text hover."""

    secrets: Any | MISSING = MISSING
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
        "emoji": Emoji,
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


@dataclass(frozen=True, slots=True)
class PresenceUpdate(Model):
    """Represent presence infomation sent in the identify payload."""

    since: int | None | MISSING = MISSING
    """Unix time (in milliseconds) of when the user went idle, \
    or [`None`][] if the user is not idle.
    """

    activities: tuple[Activity, ...] | MISSING = MISSING
    """The user's activities."""

    status: enums.Status | MISSING = MISSING
    """The user's [`status`][zcord.enums.Status]."""

    afk: bool | MISSING = MISSING
    """Whether the user is afk."""

    _transforms: ClassVar[dict] = {
        "activities": Activity,
        "status": enums.Status,
    }

    @overload
    @classmethod
    def new(
        cls,
        *,
        since: int | None | MISSING = MISSING,
        activity: Activity | MISSING = MISSING,
        status: enums.Status = enums.Status.ONLINE,
        afk: bool | MISSING = MISSING,
    ) -> PresenceUpdate: ...
    @overload
    @classmethod
    def new(
        cls,
        *,
        since: int | None | MISSING = MISSING,
        activity: types.TupleOrList[Activity] | MISSING = MISSING,
        status: enums.Status = enums.Status.ONLINE,
        afk: bool | MISSING = MISSING,
    ) -> PresenceUpdate: ...
    @classmethod
    def new(
        cls,
        *,
        since=MISSING,
        activity=MISSING,
        status=enums.Status.ONLINE,
        afk=MISSING,
    ) -> PresenceUpdate:
        """Construct a presence update object."""
        presence = cls().set_since(since).set_status(status).set_afk(afk)
        if isinstance(activity, (list, tuple)):
            presence = presence.set_activities(activity)
        elif activity is not MISSING:
            presence = presence.add_activity(activity)
        return presence

    def set_since(
        self, since: int | None | MISSING = MISSING
    ) -> PresenceUpdate:
        """Set the Unix timestamp (in milliseconds) of when the bot went \
        idle.
        """
        return set_field_value(self, "since", since)

    def set_status(
        self, status: enums.Status | MISSING = MISSING
    ) -> PresenceUpdate:
        """Set the status of the bot."""
        return set_field_value(self, "status", status)

    def set_afk(self, afk: bool | MISSING = MISSING) -> PresenceUpdate:
        """Set whether the bot is afk."""
        return set_field_value(self, "afk", afk)

    def set_activities(
        self, activities: types.TupleOrList[Activity]
    ) -> PresenceUpdate:
        """Set the bot's activities."""
        presence = self.clear_activities()
        return presence.add_activities(activities)

    def clear_activities(self) -> PresenceUpdate:
        """Clear the bot's activities."""
        return set_field_value(self, "activities", MISSING)

    def add_activities(
        self, actitivies: types.TupleOrList[Activity]
    ) -> PresenceUpdate:
        """Add multiple activities to the bot."""
        presence = self
        for a in actitivies:
            presence = self.add_activity(a)
        return presence

    def add_activity(self, activity: Activity) -> PresenceUpdate:
        return add_field_value(self, "activities", activity)
