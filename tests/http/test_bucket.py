from __future__ import annotations

from zcord.http.limits import Bucket


class FakeClock:
    """Fake monotonic clock which doesn't sleep"""

    def __init__(self) -> None:
        self.now = 0.0
        self.slept: list[float] = []

    def __call__(self) -> float:
        return self.now

    async def sleep(self, delay: float) -> None:
        self.slept.append(delay)
        self.now += delay


def make_bucket() -> tuple[Bucket, FakeClock]:
    clock = FakeClock()
    return Bucket(clock=clock, sleep=clock.sleep), clock


async def test_fresh_bucket_no_wait():
    bucket, clock = make_bucket()

    async with bucket.slot():
        pass
    bucket.update(remaining=3, reset_after=5.0)

    async with bucket.slot():
        pass

    assert clock.slept == []


async def test_acquire_waits_for_exhausted_bucket():
    bucket, clock = make_bucket()

    async with bucket.slot():
        bucket.update(remaining=0, reset_after=5.0)

    async with bucket.slot():
        pass

    assert clock.slept == [5.0]


async def test_acquire_waits_for_hold():
    bucket, clock = make_bucket()

    async with bucket.slot():
        bucket.hold(2.0)
        bucket.update(remaining=0, reset_after=5.0)

    async with bucket.slot():
        bucket.hold(1.0)

    async with bucket.slot():
        pass

    assert clock.slept == [5.0, 1.0]
