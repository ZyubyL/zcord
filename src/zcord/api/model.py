from __future__ import annotations

import dataclasses
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, ClassVar, Self, overload

from zcord.missing import MISSING

type Payload = dict[str, Any]
type Loader = Callable[[Any], Any]
type Dumper = Callable[[Any], Any]


@dataclass(frozen=True)
class Model:
    """Base class for all Discord API models."""

    __slots__ = ()

    _schema: ClassVar[tuple[_FieldSpec, ...]] = ()
    _field_names: ClassVar[tuple[str, ...]] = ()
    _transforms: ClassVar[dict[str, Any]] = {}

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        # Only compile dataclass model subclasses.
        if not dataclasses.is_dataclass(cls):
            return

        transforms: dict[str, Any] = {}
        for base in reversed(cls.__mro__):
            transforms.update(getattr(base, "_transforms", {}) or {})

        specs: list[_FieldSpec] = []
        names: list[str] = []

        for f in dataclasses.fields(cls):
            names.append(f.name)
            if f.name.startswith("_"):
                continue

            has_default = f.default is not dataclasses.MISSING
            has_factory = f.default_factory is not dataclasses.MISSING
            specs.append(
                _FieldSpec(
                    name=f.name,
                    key=f.name,
                    has_default=has_default or has_factory,
                    default=None if has_factory else f.default,
                    default_factory=None
                    if not has_factory
                    else f.default_factory,
                    load=_compile_loader(transforms.get(f.name)),
                    dump=_dump_value,
                )
            )

        cls._schema = tuple(specs)
        cls._field_names = tuple(names)

    @classmethod
    @overload
    def _from_payload(cls, payload: Payload) -> Self: ...
    @classmethod
    @overload
    def _from_payload(cls, payload: MISSING) -> MISSING: ...
    @classmethod
    def _from_payload(cls, payload: Payload | MISSING) -> Self | MISSING:
        if payload is MISSING:
            return MISSING

        kwargs: dict[str, Any] = {}
        for spec in cls._schema:
            try:
                value = payload[spec.key]
            except KeyError:
                if spec.default_factory is not None:
                    kwargs[spec.name] = spec.default_factory()
                elif spec.has_default:
                    kwargs[spec.name] = spec.default
                else:
                    kwargs[spec.name] = MISSING
                continue

            if value is None or value is MISSING:
                kwargs[spec.name] = value
            else:
                kwargs[spec.name] = spec.load(value)

        return cls(**kwargs)

    def _to_payload(self) -> Payload:
        self._check_before()
        payload: Payload = {}

        for spec in type(self)._schema:
            value = getattr(self, spec.name)
            if value is MISSING:
                continue
            dumped = spec.dump(value)
            if dumped is MISSING:
                continue
            payload[spec.key] = dumped

        return self._check_after(payload)

    def _copy(self, **changes: Any) -> Self:
        """Fast frozen copy for internal trusted updates."""
        cls = type(self)
        new = object.__new__(cls)
        for name in cls._field_names:
            if name in changes:
                object.__setattr__(new, name, changes.pop(name))
            else:
                object.__setattr__(new, name, getattr(self, name))
        if changes:
            raise TypeError(
                f"Unknown field(s) for {cls.__name__}: {','.join(changes)}"
            )
        return new

    # Python 3.13+ copy.replace() support.
    # Does nothing on 3.12.
    def __replace__(self, **changes: Any) -> Self:
        return self._copy(**changes)

    def _merge(self, other: Self) -> Self:
        changes: dict[str, Any] = {}
        for spec in type(self)._schema:
            value = getattr(other, spec.name)
            if value is not MISSING:
                changes[spec.name] = value
        return self._copy(**changes) if changes else self

    def _check_before(self) -> None:
        pass

    def _check_after(self, payload: Payload) -> Payload:
        return payload


def add_field_value[T: Model](self: T, field_name: str, value: Any) -> T:
    """Wrapper for add_* methods."""
    if isinstance(value, (tuple, list)):
        raise ValueError("Cannot add a sequence value, use a loop or set_*")

    field = getattr(self, field_name)
    if isinstance(field, tuple):
        if value is MISSING:
            raise ValueError("Cannot add MISSING to a tuple field")
        return self._copy(**{field_name: (*field, value)})
    if field is MISSING:
        return self._copy(**{field_name: (value,)})
    return self._copy(**{field_name: (field, value)})


def set_field_value[T: Model](self: T, field_name: str, value: Any) -> T:
    """Wrapper for set_* methods."""
    field = getattr(self, field_name)

    if isinstance(field, tuple):
        if isinstance(value, (tuple, list)):
            return self._copy(**{field_name: (*value,)})
        if value is MISSING:
            return self._copy(**{field_name: MISSING})
        return self._copy(**{field_name: (value,)})

    if isinstance(value, (list, tuple)):
        return self._copy(**{field_name: (*value,)})
    return self._copy(**{field_name: value})


@dataclass(frozen=True, slots=True)
class _FieldSpec:
    name: str
    key: str
    has_default: bool
    default: Any
    default_factory: Callable[[], Any] | None
    load: Loader
    dump: Dumper


def _is_missing(value: Any) -> bool:
    return value is MISSING


def _dump_value(value: Any) -> Any:
    if value is MISSING:
        return MISSING
    if isinstance(value, Model):
        return value._to_payload()
    if isinstance(value, tuple):
        if not value:
            return []
        if isinstance(value[0], Model):
            return [item._to_payload() for item in value]
        if isinstance(value[0], datetime):
            return [item.isoformat() for item in value]
        if isinstance(value[0], Enum):
            return [item.value for item in value]
        return list(value)
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    return value


def _compile_loader(transform: Any) -> Loader:
    """Compile a transform into a fast payload loader.

    Notes:
        - MISSING/None are passed through by the caller
        - If payload value is list/tuple, transform is applied per item
        - Transform may be a Model subclass or any callable, \
        e.g. Snowflake, Enum, fromisoformat,...
    """
    if transform is None:
        return lambda value: value

    if isinstance(transform, type) and issubclass(transform, Model):
        model_from_payload = transform._from_payload

        def load_model(value: Any) -> Any:
            if isinstance(value, (list, tuple)):
                return tuple(model_from_payload(item) for item in value)
            return model_from_payload(value)

        return load_model

    def load_value(value: Any) -> Any:
        if isinstance(value, (list, tuple)):
            return tuple(transform(item) for item in value)
        return transform(value)

    return load_value
