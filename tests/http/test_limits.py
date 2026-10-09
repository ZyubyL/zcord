from __future__ import annotations

from zcord.http.limits import RateLimiter

from .test_bucket import FakeClock


def make_limiter() -> tuple[RateLimiter, FakeClock]:
    clock = FakeClock()
    return RateLimiter(clock=clock, sleep=clock.sleep), clock


async def test_same_route_share_bucket():
    limiter, _ = make_limiter()

    async with limiter.slot("GET", "/channels/1/messages") as one:
        pass

    async with limiter.slot("GET", "/channels/1/messages") as two:
        pass

    assert one is two


async def test_top_level_resources_independent_buckets():
    limiter, _ = make_limiter()

    async with limiter.slot("GET", "/channels/1/messages") as one:
        pass

    async with limiter.slot("GET", "/channels/2/messages") as two:
        pass

    assert one is not two


async def test_learn_merge_route_same_bucket_hash():
    limiter, _ = make_limiter()

    limiter.learn("GET", "/guilds/1/members/9", "sharedhash")
    limiter.learn("GET", "/guilds/1/members/search", "sharedhash")

    async with limiter.slot("GET", "/guilds/1/members/9") as one:
        pass

    async with limiter.slot("GET", "/guilds/1/members/search") as two:
        pass

    assert one is two


async def test_global_hold_blocks_all_but_interactions():
    limiter, clock = make_limiter()

    limiter.hold_global(2.0)

    async with limiter.slot("GET", "/users/@me"):
        pass

    async with limiter.slot(
        "POST", "/interactions/1/tok/callback", global_limited=False
    ):
        pass

    assert clock.slept == [2.0]


async def test_global_window_blocks_over_global_limit():
    limiter, clock = make_limiter()

    for _ in range(RateLimiter.GLOBAL_LIMIT):
        async with limiter.slot("GET", "/users/@me"):
            pass

    async with limiter.slot("GET", "/users/@me"):
        pass

    assert clock.slept == [RateLimiter.GLOBAL_WINDOW]
