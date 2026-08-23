from __future__ import annotations

from datetime import UTC, datetime

import pytest

from zcord import Snowflake
from zcord.models.snowflake import DISCORD_EPOCH

EXPECTED_TIME = datetime(2026, 1, 1, tzinfo=UTC)
INPUT_VALUE = int(EXPECTED_TIME.timestamp() * 1000 - DISCORD_EPOCH) << 22
DISCORD_EPOCH_DATETIME = datetime.fromtimestamp(DISCORD_EPOCH / 1000, tz=UTC)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (INPUT_VALUE, EXPECTED_TIME),
        (0, DISCORD_EPOCH_DATETIME),
    ],
)
def test_to_datetime(value, expected):
    assert Snowflake(value).to_datetime() == expected
