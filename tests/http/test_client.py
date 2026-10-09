from __future__ import annotations

import orjson

from zcord.http.client import HTTPClient
from zcord.http.limits import RateLimiter

from .test_limits import FakeClock

TOKEN = "mock.token"


class ResponseMock:
    """Mock API response with ratelimit headers"""

    def __init__(
        self,
        *,
        status: int = 200,
        body: object = {},
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status = status
        self.ok = status < 400
        self.reason = "OK" if self.ok else "Too Many Requests"
        self.headers = headers or {}
        self._body = orjson.dumps(body) if body is not None else b""

    async def read(self) -> bytes:
        return self._body


class RequestMock:
    """Async context manager yielding the canned response"""

    def __init__(self, response: ResponseMock) -> None:
        self._response = response

    async def __aenter__(self) -> ResponseMock:
        return self._response

    async def __aexit__(self, *exc: object) -> bool:
        return False


class SessionMock:
    """Mock session with scripted responses"""

    closed = False

    def __init__(self, responses: list[ResponseMock]) -> None:
        self._responses = iter(responses)

    def request(self, method: str, url: str, *, json=None) -> RequestMock:
        return RequestMock(next(self._responses))


def make_client(responses: list[ResponseMock]) -> tuple[HTTPClient, FakeClock]:
    clock = FakeClock()
    client = HTTPClient(
        TOKEN, limiter=RateLimiter(clock=clock, sleep=clock.sleep)
    )
    client._session = SessionMock(responses)  # type: ignore
    return client, clock


def ratelimit_headers(remaining: int, reset_after: float) -> dict[str, str]:
    return {
        "X-RateLimit-Bucket": "mockbucket",
        "X-RateLimit-Remaining": str(remaining),
        "X-RateLimit-Reset-After": str(reset_after),
    }


async def test_respect_exhausted_bucket_headers():
    client, clock = make_client(
        [
            ResponseMock(body={"id": "1"}, headers=ratelimit_headers(0, 5.0)),
            ResponseMock(body={"id": "1"}),
        ]
    )

    first = await client.request("GET", "/users/@me")
    second = await client.request("GET", "/users/@me")

    assert first == second == (200, {"id": "1"})
    assert clock.slept == [5.0]


async def test_retry_after_429():
    client, clock = make_client(
        [
            ResponseMock(
                status=429,
                body={
                    "message": "You are being rate limited.",
                    "retry_after": 2.0,
                    "global": False,
                },
            ),
            ResponseMock(body={"id": "1"}),
        ]
    )

    result = await client.request("GET", "/users/@me")

    assert result == (200, {"id": "1"})
    assert clock.slept == [2.0]


async def test_global_429_hold_all_routes():
    limited = ResponseMock(
        status=429,
        body={
            "message": "You are being rate limnited.",
            "retry_after": 1.0,
            "global": True,
        },
    )
    client, clock = make_client([limited, limited, limited, ResponseMock()])

    result = await client.request("GET", "/users/@me")
    other_route = await client.request("GET", "/channels/1/messages")

    # After waited 3 times, give up
    assert result == (429, "Rate limited after max retries")
    assert clock.slept == [1.0, 1.0, 1.0]
    assert other_route == (200, {})
