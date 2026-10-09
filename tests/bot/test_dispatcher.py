from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING

from zcord.bot import EventDispatcher

if TYPE_CHECKING:
    from pytest import LogCaptureFixture

EVENT = "MESSAGE_CREATE"


def test_listeners():
    dispatcher = EventDispatcher()
    calls: list[str] = []

    dispatcher.register(EVENT, lambda: calls.append("once"), once=True)
    dispatcher.register(EVENT, lambda: calls.append("persistent"), once=False)

    dispatcher.dispatch(EVENT, ())
    # The one-time listener should be gone in the second dispatch
    dispatcher.dispatch(EVENT, ())

    assert calls == ["once", "persistent", "persistent"]


def test_failing_listener_blocking(caplog: LogCaptureFixture):
    dispatcher = EventDispatcher()
    calls: list[str] = []

    def kaboom() -> None:
        raise ValueError("this listener is up to no good")

    with caplog.at_level(logging.ERROR):
        dispatcher.register(EVENT, kaboom, once=False)
        dispatcher.register(EVENT, lambda: calls.append("normal"), once=False)
        dispatcher.dispatch(EVENT, ())
        dispatcher.dispatch(EVENT, ())

    assert calls == ["normal", "normal"]

    assert "Failed to dispatch event" in caplog.text


async def test_failing_async_listener_logging(caplog: LogCaptureFixture):
    dispatcher = EventDispatcher()

    async def kaboom() -> None:
        raise ValueError("this async listener is broken")

    with caplog.at_level(logging.ERROR):
        dispatcher.register(EVENT, kaboom, once=False)
        dispatcher.dispatch(EVENT, ())
        await asyncio.gather(*dispatcher._tasks, return_exceptions=True)

    assert "Failed to dispatch event" in caplog.text
