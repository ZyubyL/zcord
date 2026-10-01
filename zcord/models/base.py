from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from zcord.missing import MISSING


def _apply_transform(transform: Any, value: Any) -> Any:
    if hasattr(transform, "_from_payload"):
        return transform._from_payload(value)
    return transform(value)


def from_payload(cls, payload: dict | MISSING, **transforms) -> Any:
    if payload is MISSING:
        return MISSING
    kwargs = {}
    for f in dataclasses.fields(cls):
        # Skipping private fields
        if f.name.startswith("_"):
            continue
        value = payload.get(f.name, f.default)
        if (
            f.name in transforms
            and value is not None
            and value is not f.default
        ):
            t = transforms[f.name]
            if isinstance(value, (tuple, list)):
                value = tuple(_apply_transform(t, v) for v in value)
            # NOTE: This doesn't work for stacked payload objects
            # NOTE: Maybe I could find a better way to do it.

            # elif isinstance(value, dict):
            #     ktype, vtype = typing.get_args(t)
            #     value = {
            #         _apply_transform(ktype, k): _apply_transform(vtype, v)
            #         for k, v in value.items()
            #     }
            else:
                value = _apply_transform(t, value)
        kwargs[f.name] = value
    return cls(**kwargs)


def add_field_value(cls, field_name: str, value: Any) -> Any:
    """Wrapper to all the add_* methods

    Notes:
        Value is not a sequence type
    """
    field = getattr(cls, field_name)
    if isinstance(field, tuple):
        replace = {field_name: (*field, value)}
    elif field is MISSING:
        replace = {field_name: (value,)}
    else:
        replace = {field_name: (field, value)}
    return dataclasses.replace(cls, **replace)


def set_field_value(cls, field_name: str, value: Any) -> Any:
    """Wrapper for all the set_* methods"""
    field = getattr(cls, field_name)
    if isinstance(field, tuple):
        if isinstance(value, (tuple, list)):
            replace = {field_name: (*value,)}
        else:
            replace = {field_name: (value,)}
    else:
        replace = {field_name: value}
    return dataclasses.replace(cls, **replace)


class Model:
    """
    Base class for all Discord API Models.
    """

    def __int__(self) -> int:
        if hasattr(self, "id") and isinstance(self.id, int):
            return self.id
        raise TypeError(f"Cannot convert {type(self).__name__!r} to int")

    @classmethod
    def _from_payload(cls, payload):
        return from_payload(cls, payload, **getattr(cls, "_transforms", {}))

    def _check_before(self) -> None:
        pass

    def _check_after(self, payload: dict) -> dict:
        return payload

    def _to_payload(self) -> dict:
        self._check_before()
        payload = {}
        for f in dataclasses.fields(self):  # type: ignore
            # Same as from_payload, we will skip private fields
            if f.name.startswith("_"):
                continue
            value = getattr(self, f.name)
            if value is MISSING:
                continue
            # Nested ZcordModel
            if isinstance(value, Model):
                payload[f.name] = value._to_payload()
            # Nested list of ZcordModel
            elif (
                isinstance(value, tuple)
                and value
                and isinstance(value[0], Model)
            ):
                # Convert back to list to send
                payload[f.name] = [item._to_payload() for item in value]
            elif isinstance(value, datetime):
                payload[f.name] = value.isoformat()
            else:
                payload[f.name] = value
        payload = self._check_after(payload)
        return payload
