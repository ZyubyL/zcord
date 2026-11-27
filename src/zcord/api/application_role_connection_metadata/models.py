from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.model import Model
from zcord.missing import MISSING


@dataclass(frozen=True, slots=True)
class ApplicationRoleConnectionMetadata(Model):
    type: enums.ApplicationRoleConnectionMetadataType
    """Type of metadata value."""

    key: str
    """Dictionary key for the metadata field."""

    name: str
    """Name of the metadata field."""

    description: str
    """Description of the metadata."""

    name_localizations: dict | MISSING = MISSING
    """Translations of the name."""

    description_localizations: dict | MISSING = MISSING
    """Translations of the description."""

    _transforms: ClassVar[dict[str, Any]] = {
        "type": enums.ApplicationRoleConnectionMetadataType
    }
