from __future__ import annotations

from collections import OrderedDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zcord.models.message import Message
    from zcord.models.snowflake import Snowflake


class SnowflakeStore[T]:
    """Store all objects keyed by [`Snowflake`][] ID."""

    def __init__(self) -> None:
        self._items: dict[int, T] = {}

    def get(self, key: int | Snowflake) -> T | None:
        """
        Returns:
            The stored object.
            Or [`None`][] if absent.
        """
        return self._items.get(key)

    def set(self, key: int | Snowflake, value: T) -> None:
        """Store `value` under `key`, replacing any existing object."""
        self._items[key] = value

    def remove(self, key: int | Snowflake) -> T | None:
        """Remove and return the stored object, or [`None`][] is absent."""
        return self._items.pop(key, None)

    def all(self) -> tuple[T, ...]:
        """
        Returns:
            All stored objects.
        """
        return tuple(self._items.values())

    def __len__(self) -> int:
        return len(self._items)


class MessageStore:
    """Bounded store of messages keyed by `(channel_id, message_id)`.

    Notes:
        Evicts the least recently used message once `max_messages` is \
        exceeded. Accessing a message refreshes its recency.
    """

    def __init__(self, max_messages: int = 1000) -> None:
        """
        Args:
            max_messages:
                The maximum number of messages to keep.

        Raises:
            ValueError:
                `max_messages` is less than 1.
        """
        if max_messages < 1:
            raise ValueError("max_messages must be at least 1")
        self._max_messages = max_messages

        self._items: OrderedDict[tuple[int, int], Message] = OrderedDict()

    def get(
        self, channel_id: int | Snowflake, message_id: int | Snowflake
    ) -> Message | None:
        """
        Returns:
            The stored message.
            Or [`None`][] if absent.
        """
        key = (channel_id, message_id)
        message = self._items.get(key)
        if message is not None:
            self._items.move_to_end(key)
        return message

    def set(
        self,
        channel_id: int | Snowflake,
        message_id: int | Snowflake,
        message: Message,
    ) -> None:
        """Store `message`, replacing any existing one.

        Notes:
            Evicts the least recently used message when over capacity.
        """
        key = (channel_id, message_id)
        self._items[key] = message
        self._items.move_to_end(key)
        if len(self._items) > self._max_messages:
            self._items.popitem(last=False)

    def remove(
        self, channel_id: int | Snowflake, message_id: int | Snowflake
    ) -> Message | None:
        """Remove and return the stored message, or [`None`][] if absent."""
        return self._items.pop((channel_id, message_id), None)

    def all(self) -> tuple[Message, ...]:
        """
        Returns:
            All stored messages.
        """
        return tuple(self._items.values())

    def __len__(self) -> int:
        return len(self._items)
