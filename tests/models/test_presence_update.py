from __future__ import annotations

from zcord import MISSING, Activity, PresenceUpdate


def test_activities_stacking():
    presence = PresenceUpdate.new(
        activity=[Activity.new(name="one"), Activity.new(name="two")]
    )

    assert presence.activities is not MISSING
    assert [a.name for a in presence.activities] == ["one", "two"]


def test_activity_timestamps():
    unix_timestamp_millis = 15112000660000
    activity = Activity._from_payload(
        {"name": "foo", "timestamps": {"start": unix_timestamp_millis}}
    )

    assert activity.timestamps is not MISSING
    assert activity.timestamps.start == unix_timestamp_millis
    assert (
        activity._to_payload()["timestamps"]["start"] == unix_timestamp_millis
    )
