from __future__ import annotations

import asyncio
import time
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, Awaitable, Callable


_MAJOR_RESOURCES = ("channels", "guilds", "webhooks")


def _route_key(method: str, endpoint: str) -> str:
    """
    Route identity
    """
    major = False
    key = []
    for part in endpoint.split("?")[0].split("/"):
        if part.isdigit() and not major:
            key.append("*")
        else:
            key.append(part)
        major = part in _MAJOR_RESOURCES
    return f"{method} {'/'.join(key)}"


def _major_key(endpoint: str) -> str:
    """
    The top level resources this route's limits count against.
    """
    parts = endpoint.split("?")[0].split("/")
    majors = [
        f"{part}/{parts[i + 1]}"
        for i, part in enumerate(parts)
        if part in _MAJOR_RESOURCES and i + 1 < len(parts)
    ]
    return " ".join(majors)


class RateLimiter:
    """Hold the global gate and one ['Bucket`][] per rate limit"""

    GLOBAL_LIMIT: Final = 50
    """Requests/second per bot"""
    GLOBAL_WINDOW: Final = 1.0

    def __init__(
        self,
        *,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        """
        Params:
            clock:
                Injectable monotonic time source.
            sleep:
                Injectable sleep implementation to wait for limits.
        """
        self._clock = clock
        self._sleep = sleep
        self._buckets: dict[str, Bucket] = {}
        self._hashes: dict[str, str] = {}
        self._global_remaining = self.GLOBAL_LIMIT
        self._global_reset_at = 0.0
        self._global_hold_util = 0.0

    @asynccontextmanager
    async def slot(
        self, method: str, endpoint: str, *, global_limited: bool = True
    ) -> AsyncGenerator[Bucket]:
        """
        Hold a request slot:
            - Wait for global limit and route's bucket
            - Yield the bucket to sync state before release.

        Params:
            global_limited:
                `False` for interaction endpoints, which are exempt \
                from global rate limit.
        """
        if global_limited:
            await self._global_acquire()
        bucket = self._bucket(method, endpoint)
        async with bucket.slot():
            yield bucket

    def learn(
        self, method: str, endpoint: str, bucket_hash: str | None
    ) -> None:
        """
        Group the route under its `X-RateLimit-Bucket` hash so shared limits \
        share single bucket.
        """
        route = _route_key(method, endpoint)
        if not bucket_hash or self._hashes.get(route) == bucket_hash:
            return
        old_key = self._bucket_key(method, endpoint)
        self._hashes[route] = bucket_hash
        new_key = self._bucket_key(method, endpoint)
        moved = self._buckets.pop(old_key, None)
        self._buckets.setdefault(
            new_key, moved if moved is not None else self._make_bucket()
        )

    def hold_global(self, retry_after: float) -> None:
        """
        Pause all global limited requests.
        """
        now = self._clock()
        self._global_hold_util = max(self._global_hold_util, now + retry_after)

    async def _global_acquire(self) -> None:
        while True:
            now = self._clock()
            if now >= self._global_reset_at:
                self._global_remaining = self.GLOBAL_LIMIT
                self._global_reset_at = now + self.GLOBAL_WINDOW
            if self._global_hold_util > now:
                await self._sleep(self._global_hold_util - now)
                continue
            if self._global_remaining > 0:
                self._global_remaining -= 1
                return
            await self._sleep(self._global_reset_at - now)

    def _bucket(self, method: str, endpoint: str) -> Bucket:
        key = self._bucket_key(method, endpoint)
        if key not in self._buckets:
            self._buckets[key] = self._make_bucket()
        return self._buckets[key]

    def _bucket_key(self, method: str, endpoint: str) -> str:
        route = _route_key(method, endpoint)
        ident = self._hashes.get(route, route)
        return f"{ident} {_major_key(endpoint)}"

    def _make_bucket(self) -> Bucket:
        return Bucket(clock=self._clock, sleep=self._sleep)


class Bucket:
    """Ratelimit state for Discord from response headers"""

    def __init__(
        self,
        *,
        clock: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ) -> None:
        """
        Params:
            clock:
                Injectable monotonic time source.
            sleep:
                Injectable sleep implementation to wait for limits.
        """
        self._clock = clock
        self._sleep = sleep

        self._lock = asyncio.Lock()
        self._remaining = 1
        self._reset_at = 0.0
        self._hold_until = 0.0

    @asynccontextmanager
    async def slot(self) -> AsyncGenerator[None]:
        """
        Hold one request slot:
            - Wait for capacity.
            - Yield while request is in flight.
            - Serialize requests within the bucket.
        """
        async with self._lock:
            await self._wait_ready()
            yield

    async def _wait_ready(self) -> None:
        while True:
            now = self._clock()
            blocked_until = self._hold_until
            if self._remaining <= 0:
                blocked_until = max(blocked_until, self._reset_at)
            if blocked_until <= now:
                return
            await self._sleep(blocked_until - now)

    def update(self, *, remaining: int, reset_after: float) -> None:
        """
        Sync state from `X-RateLimit-Remaining` / `X-RateLimit-Reset-After`.
        """
        self._remaining = remaining
        self._reset_at = self._clock() + reset_after

    def hold(self, retry_after: float) -> None:
        """
        Block the bucket until `retry_after` elapses.
        """
        self._hold_until = max(self._hold_until, self._clock() + retry_after)
