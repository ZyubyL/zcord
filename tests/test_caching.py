from __future__ import annotations

from zcord import MISSING
from zcord.caching import MessageStore, SnowflakeStore
from zcord.enums import GatewayEvent
from zcord.models import Guild, Message
from zcord.state import ConnectionState

CHANNEL_ID = 123
GUILD_ID = 456
MESSAGE_ID = 789
AUTHOR_ID = 67
MAX_MESSAGES = 2


def make_guild(guild_id: int = GUILD_ID) -> Guild:
    return Guild._from_payload({"id": str(guild_id), "name": "test"})


def make_message(message_id: int) -> Message:
    return Message._from_payload(
        {"id": str(message_id), "channel_id": str(CHANNEL_ID)}
    )


def test_snowflake_store():
    store = SnowflakeStore[Guild]()
    guild = make_guild()
    store.set(guild.id, guild)

    assert store.get(guild.id) is guild
    assert store.all() == (guild,)
    assert len(store) == 1

    assert store.remove(guild.id) is guild
    assert store.get(guild.id) is None


def test_message_store_evicts_lru():
    store = MessageStore(max_messages=MAX_MESSAGES)
    first, second, third = map(make_message, (1, 2, 3))
    assert first.id is not MISSING
    assert second.id is not MISSING
    assert third.id is not MISSING
    store.set(CHANNEL_ID, first.id, first)
    store.set(CHANNEL_ID, second.id, second)
    store.set(CHANNEL_ID, third.id, third)

    assert store.get(CHANNEL_ID, first.id) is None
    assert store.all() == (second, third)
    assert len(store) == 2


def test_message_store_get_do_refresh_lru():
    store = MessageStore(max_messages=MAX_MESSAGES)
    first, second, third = map(make_message, (1, 2, 3))
    assert first.id is not MISSING
    assert second.id is not MISSING
    assert third.id is not MISSING
    store.set(CHANNEL_ID, first.id, first)
    store.set(CHANNEL_ID, second.id, second)

    assert store.get(CHANNEL_ID, first.id) is first

    store.set(CHANNEL_ID, third.id, third)

    assert store.get(CHANNEL_ID, second.id) is None
    assert store.get(CHANNEL_ID, first.id) is first


def test_update_cache_populates_stores():
    state = ConnectionState("mock.token")

    state._update_cache(
        str(GatewayEvent.GUILD_CREATE),
        {
            "id": str(GUILD_ID),
            "name": "test",
            "channels": [{"id": str(CHANNEL_ID)}],
        },
    )
    state._update_cache(
        str(GatewayEvent.MESSAGE_CREATE),
        {
            "id": str(MESSAGE_ID),
            "channel_id": str(CHANNEL_ID),
            "author": {"id": str(AUTHOR_ID), "username": "zcord"},
        },
    )

    assert state.guilds.get(GUILD_ID) is not None
    assert state.channels.get(CHANNEL_ID) is not None
    assert state.messages.get(CHANNEL_ID, MESSAGE_ID) is not None
    assert state.users.get(AUTHOR_ID) is not None
