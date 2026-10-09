from __future__ import annotations

from zcord.bot import EventConverter
from zcord.enums import GatewayEvent
from zcord.models import Guild, User
from zcord.state import ConnectionState

READY = str(GatewayEvent.READY)
GUILD_UPDATE = str(GatewayEvent.GUILD_UPDATE)
RESUMED = str(GatewayEvent.RESUMED)

USER = {
    "id": "123",
    "username": "zcord",
    "discriminator": "0",
    "global_name": None,
    "avatar": None,
}


def make_converter() -> EventConverter:
    return EventConverter(ConnectionState("mock.token"))


def test_ready_payload_unwrap_to_user():
    converter = make_converter()

    args = converter.convert(
        READY,
        {
            "session_id": "abc",
            "resume_gateway_url": "wss://gateway.test",
            "user": USER,
        },
    )

    # READY event should only forward User object
    assert len(args) == 1

    user = args[0]
    assert isinstance(user, User)
    assert user.username == USER["username"]


def test_update_event_args():
    state = ConnectionState("mock.token")
    old = Guild._from_payload({"id": "456", "name": "before"})
    state._guilds[456] = old
    converter = EventConverter(state)

    old_arg, new = converter.convert(
        GUILD_UPDATE, {"id": "456", "name": "after"}
    )

    assert old_arg is old
    assert isinstance(new, Guild)
    assert new.name == "after"


def test_unregistered_event_fall_through():
    converter = make_converter()

    assert converter.convert(RESUMED, None) == (None,)
