from __future__ import annotations

import zlib

import pytest

from zcord.gateway import ZlibStream

SUFFIX = b"\x00\x00\xff\xff"
HELLO = b'{"op":10,"d":{"heartbeat_interval":41250}}'
READY = b'{"op":0,"t":"READY","s":1,"d":{}}'
GUILD_CREATE = b'{"op":0,"t":"GUILD_CREATE","s":2,"d":{"id":"123"}}'

MESSAGES = [HELLO, READY, GUILD_CREATE]


class DiscordWireMock:
    """Mock Discord zlib-stream wire"""

    def __init__(self) -> None:
        self._compressor = zlib.compressobj()

    def send(self, message: bytes) -> bytes:
        return self._compressor.compress(message) + self._compressor.flush(
            zlib.Z_SYNC_FLUSH
        )


def test_burst_in_one_frame_returns_messages_in_order():
    handler = ZlibStream()
    wire = DiscordWireMock()

    data = b"".join(wire.send(message) for message in MESSAGES)
    assert handler.feed(data) == MESSAGES


def test_suffix_stradding_frames_buffers_until_complete():
    handler = ZlibStream()
    wire = DiscordWireMock()
    data = wire.send(HELLO)
    cut = len(data) - 2
    assert handler.feed(data[:cut]) == []
    assert handler.feed(data[cut:]) == [HELLO]


def test_corrupt_data_raises_and_reset_stream():
    handler = ZlibStream()
    with pytest.raises(zlib.error):
        handler.feed(b"garbage" + SUFFIX)
    handler.reset()
    wire = DiscordWireMock()
    assert handler.feed(wire.send(HELLO)) == [HELLO]


def test_streams_are_isolated():
    one, two = ZlibStream(), ZlibStream()
    wire_one, wire_two = DiscordWireMock(), DiscordWireMock()

    payload_one = wire_one.send(HELLO)
    cut_one = len(payload_one) - 2
    assert one.feed(payload_one[:cut_one]) == []

    # This does not affect the other handler
    assert two.feed(wire_two.send(READY)) == [READY]

    assert one.feed(payload_one[cut_one:]) == [HELLO]
