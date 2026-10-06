from __future__ import annotations

from zcord.gateway import Backoff

JITTER = 0.5
STEP = Backoff.DELAY_STEP
CAP = Backoff.DELAY_CAP
MAX_FAILURES = Backoff.MAX_CONNECT_FAILURES


def test_connect_failures_give_up_then_recover():
    backoff = Backoff(rng=lambda: JITTER)
    given_up = [backoff.record_connect_failure() for _ in range(MAX_FAILURES)]
    assert given_up == [False] * (MAX_FAILURES - 1) + [True]

    backoff.record_connect_success()
    assert backoff.connect_failures == 0
    assert backoff.record_connect_failure() is False


def test_reconnect_delay_grows_to_caps_and_reset_on_ready():
    backoff = Backoff(rng=lambda: JITTER)
    assert backoff.reconnect_delay == JITTER

    backoff.increase_delay()
    assert backoff.reconnect_delay == STEP + JITTER

    for _ in range(int(CAP / STEP)):
        backoff.increase_delay()
    assert backoff.reconnect_delay == CAP + JITTER

    backoff.reset_delay()
    assert backoff.reconnect_delay == JITTER
