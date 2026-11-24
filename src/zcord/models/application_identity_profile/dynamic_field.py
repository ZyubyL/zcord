from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.models.application_identity_profile.media import Media
from zcord.models.base import Model


def _dynamic_field_value(value: Any) -> str | float | Media:
    if isinstance(value, dict):
        return Media._from_payload(value)
    try:
        return float(value)
    except ValueError:
        return str(value)


@dataclass(frozen=True, slots=True)
class DynamicField(Model):
    type: enums.DynamicFieldType
    """Field type."""

    name: str
    """Field name."""

    value: str | float | Media
    """Field value.

    This field type is:
        - [`str`][] when `type` is \
        [`enums.DynamicFieldTypes.STRING`][zcord.enums.DynamicFieldTypes.STRING].
        - [`float`][] when `type` is \
        [`enums.DynamicFieldTypes.NUMBER`][zcord.enums.DynamicFieldTypes.NUMBER].
        - [`Media`][] when `type` is \
        [`enums.DynamicFieldTypes.MEDIA`][zcord.enums.DynamicFieldTypes.MEDIA].
    """

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.DynamicFieldType,
        "value": _dynamic_field_value,
    }
