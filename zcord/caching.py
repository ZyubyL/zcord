from __future__ import annotations

from collections import OrderedDict
from typing import TYPE_CHECKING

from zcord.missing import MISSING

if TYPE_CHECKING:
    from zcord.models.snowflake import Snowflake


class SnowflakeStore[T]:
    """Store all objects keyed by [`Snowflake`][] ID."""

    def __init__(self) -> None:
        self._items: dict[int, T] = {}

    def _make_key(self, key: int | Snowflake | None | MISSING) -> int | None:
        if key is None or key is MISSING:
            return None
        return int(key)

    def get(self, key: int | Snowflake | None | MISSING) -> T | None:
        """
        Returns:
            The stored object.
            Or [`None`][] if absent.
        """
        if (key := self._make_key(key)) is None:
            return None
        return self._items.get(key)

    def set(self, key: int | Snowflake | None | MISSING, value: T) -> None:
        """Store `value` under `key`, replacing any existing object."""
        if (key := self._make_key(key)) is None:
            return
        self._items[key] = value

    def remove(self, key: int | Snowflake | None | MISSING) -> T | None:
        """Remove and return the stored object, or [`None`][] is absent."""
        if (key := self._make_key(key)) is None:
            return
        return self._items.pop(key, None)

    def all(self) -> tuple[T, ...]:
        """
        Returns:
            All stored objects.
        """
        return tuple(self._items.values())

    def __len__(self) -> int:
        return len(self._items)


class PairStore[T]:
    """Store objects keyed by a pair of IDs.

    Notes:
        first key is the ID from an attribute of the value.
        second key is the ID of the value.
    """

    def __init__(self, max_items: int | None = None) -> None:
        """
        Args:
            max_items:
                Maximum number of objects to keep, or [`None`][] for \
                unbounded.

        Raises:
            ValueError:
                `max_items` is less than 1.
        """
        if max_items is not None and max_items < 1:
            raise ValueError("max_items must be at least 1")

        self._max_items = max_items
        self._items: OrderedDict[tuple[int, int], T] = OrderedDict()

    def _make_key(
        self,
        first: int | Snowflake | None | MISSING,
        second: int | Snowflake | None | MISSING,
    ) -> tuple[int, int] | None:
        if (
            first is None
            or first is MISSING
            or second is None
            or second is MISSING
        ):
            return None
        return (int(first), int(second))

    def get(
        self,
        first: int | Snowflake | None | MISSING,
        second: int | Snowflake | None | MISSING,
    ) -> T | None:
        """
        Returns:
            The stored object.
            Or [`None`][] if absent.
        """
        if (key := self._make_key(first, second)) is None:
            return None
        value = self._items.get(key)
        if value is not None:
            self._items.move_to_end(key)
        return value

    def get_all_from_first_key(
        self,
        first: int | Snowflake | None | MISSING,
    ) -> tuple[T, ...] | None:
        """
        Returns:
            The stored object with the first key.
            Or [`None`][] if absent.
        """
        values: list[T] = []
        keys: list[tuple[int, int]] = []
        for (f, s), value in self._items.items():
            if f == first:
                key = self._make_key(f, s)
                assert key is not None
                keys.append(key)
                values.append(value)
        for key in keys:
            self._items.move_to_end(key)
        return None if not values else tuple(values)

    def set(
        self,
        first: int | Snowflake | None | MISSING,
        second: int | Snowflake | None | MISSING,
        value: T,
    ) -> None:
        """Store `value`, replacing any existing one.

        Notes:
            Evicts the LRU object when over capacity.
        """
        if (key := self._make_key(first, second)) is None:
            return
        self._items[key] = value
        self._items.move_to_end(key)
        if self._max_items is not None and len(self._items) > self._max_items:
            self._items.popitem(last=False)

    def remove(
        self,
        first: int | Snowflake | None | MISSING,
        second: int | Snowflake | None | MISSING,
    ) -> T | None:
        """Remove and return the stored obejct, or [`None`][] if absent."""
        if (key := self._make_key(first, second)) is None:
            return None
        return self._items.pop(key, None)

    def all(self) -> tuple[T, ...]:
        """
        Returns:
            All stored objects.
        """
        return tuple(self._items.values())

    def __len__(self) -> int:
        return len(self._items)
