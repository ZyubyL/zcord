from __future__ import annotations

import aiohttp
import orjson

from zcord.errors import HTTPError


class HTTPClient:
    BASE_URL = "https://discord.com/api/v10"

    def __init__(self, token: str) -> None:
        self._token = token
        self._session: aiohttp.ClientSession | None = None

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={"Authorization": "Bot " + self._token}
            )
        return self._session

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()
            self._session = None

    async def request(
        self, method: str, endpoint: str, *, json: dict | list | None = None
    ) -> tuple[int, dict | list[dict] | None]:
        """
        Perform a HTTP request.

        Returns:
            A tuple of the HTTP status code and the response JSON.

        Raises:
            HTTPError:
                The request returned a non-OK status code.
        """
        async with self.session.request(
            method, self.BASE_URL + endpoint, json=json
        ) as resp:
            if resp.ok:
                if resp.status == 204:
                    return resp.status, None
                return resp.status, orjson.loads(await resp.read())
            raise HTTPError(f"{resp.status} {resp.reason}")
