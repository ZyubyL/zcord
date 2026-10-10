from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Final

import aiohttp
import orjson

from zcord._version import __version__
from zcord.http.limits import Bucket, RateLimiter

if TYPE_CHECKING:
    from collections.abc import Mapping

log = logging.getLogger(__name__)

_H_BUCKET = "X-RateLimit-Bucket"
_H_REMAINING = "X-RateLimit-Remaining"
_H_RESET_AFTER = "X-RateLimit-Reset-After"
_H_RETRY_AFTER = "Retry-After"
_H_SCOPE = "X-RateLimit-Scope"

_INTERACTIONS = "/interactions/"


def _sync_headers(bucket: Bucket, headers: Mapping[str, str]) -> None:
    """Feed `X-RateLimit-*` response headers into the bucket."""
    remaining = headers.get(_H_REMAINING)
    reset_after = headers.get(_H_RESET_AFTER)

    if remaining is not None and reset_after is not None:
        bucket.update(remaining=int(remaining), reset_after=float(reset_after))


async def _read_ratelimit(resp: aiohttp.ClientResponse) -> tuple[float, bool]:
    """
    Parse 429 feedback.

    Returns:
        Seconds to wait, and whether the limit is global.
    """
    try:
        body = orjson.loads(await resp.read())
    except orjson.JSONDecodeError:
        body = {}  # CF bans return non-JSON bodies

    retry_after = body.get("retry_after")
    if retry_after is None:
        retry_after = resp.headers.get(_H_RETRY_AFTER, 1.0)

    is_global = (
        body.get("global") is True or resp.headers.get(_H_SCOPE) == "global"
    )
    return float(retry_after), is_global


class HTTPClient:
    BASE_URL = "https://discord.com/api/v10"
    MAX_RETRIES: Final = 3

    def __init__(
        self, token: str, *, limiter: RateLimiter | None = None
    ) -> None:
        """
        Params:
            token:
                The bot token.
            limiter:
                Injectable rate limit state.
        """
        self._token = token
        self._limiter = limiter or RateLimiter()

        self._session: aiohttp.ClientSession | None = None

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={
                    "Authorization": "Bot " + self._token,
                    "User-Agent": (
                        "DiscordBot (https://github.com/zyubyl/zcord,"
                        f" {__version__}"
                    ),
                }
            )
        return self._session

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()
            self._session = None

    async def _handle_429(
        self,
        method: str,
        endpoint: str,
        resp: aiohttp.ClientResponse,
        bucket: Bucket,
    ) -> None:
        retry_after, is_global = await _read_ratelimit(resp)
        if is_global:
            self._limiter.hold_global(retry_after)
        else:
            bucket.hold(retry_after)
        log.warning(
            "Rate limited on %s %s (%s), retrying in %.2f seconds",
            method,
            endpoint,
            "global" if is_global else _H_SCOPE,
            retry_after,
        )

    async def request(
        self, method: str, endpoint: str, *, json: dict | list | None = None
    ) -> tuple[int, dict | list[dict] | str | None]:
        """
        Perform a HTTP request.

        Returns:
            A tuple of the HTTP status code and the response JSON.
            Or a tuple of the HTTP status code and the error message.
        """
        log.debug("%s %s", method, endpoint)
        for _ in range(self.MAX_RETRIES):
            global_limited = not endpoint.startswith(_INTERACTIONS)
            async with (
                self._limiter.slot(
                    method, endpoint, global_limited=global_limited
                ) as bucket,
                self.session.request(
                    method, self.BASE_URL + endpoint, json=json
                ) as resp,
            ):
                self._limiter.learn(
                    method, endpoint, resp.headers.get(_H_BUCKET)
                )
                _sync_headers(bucket, resp.headers)

                if resp.status == 429:
                    await self._handle_429(method, endpoint, resp, bucket)
                    continue

                if resp.ok:
                    log.debug("%s %s: %d", method, endpoint, resp.status)
                    if resp.status == 204:
                        return resp.status, None
                    return resp.status, orjson.loads(await resp.read())

                log.debug(
                    "%s %s: %d %s",
                    method,
                    endpoint,
                    resp.status,
                    resp.reason,
                )
                return resp.status, resp.reason

        return 429, "Rate limited after max retries"
