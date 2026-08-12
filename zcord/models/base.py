from __future__ import annotations

import dataclasses
from datetime import datetime
from typing import Any

from zcord.missing import MISSING


def _apply_transform(transform, value):
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
            if isinstance(value, list):
                value = [_apply_transform(t, v) for v in value]
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


class ZcordModel:
    """
    Base class for all Discord API Models.
    """

    def __int__(self):
        if hasattr(self, "id"):
            return self.id

    @classmethod
    def _from_payload(cls, payload):
        return from_payload(cls, payload, **getattr(cls, "_transforms", {}))

    def _to_payload(self) -> dict:
        payload = {}
        for f in dataclasses.fields(self):  # type: ignore
            # Same as from_payload, we will skip private fields
            if f.name.startswith("_"):
                continue
            value = getattr(self, f.name)
            if value is MISSING:
                continue
            # Nested ZcordModel
            if isinstance(value, ZcordModel):
                payload[f.name] = value._to_payload()
            # Nested list of ZcordModel
            elif (
                isinstance(value, list)
                and value
                and isinstance(value[0], ZcordModel)
            ):
                payload[f.name] = [item._to_payload() for item in value]
            elif isinstance(value, datetime):
                payload[f.name] = value.isoformat()
            else:
                payload[f.name] = value
        return payload
