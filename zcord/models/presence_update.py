from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar, overload

from zcord import enums, types
from zcord.missing import MISSING
from zcord.models.activity.activity import Activity
from zcord.models.base import Model, add_field_value, set_field_value


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
