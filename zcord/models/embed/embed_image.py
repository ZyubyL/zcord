from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedImage(Model):
    """
    Contain embed's image info.
    """

    url: str
    """
    Source URL of the image.
    """

    proxy_url: str | MISSING = MISSING
    """
    A proxied URL of the image.
    """

    height: int | MISSING = MISSING
    """
    The image's height.
    """

    width: int | MISSING = MISSING
    """
    The image's width.
    """

    content_type: str | MISSING = MISSING
    """
    The image's media type.
    """

    placeholder: str | MISSING = MISSING
    """
    Thumbhash placeholder of the image.
    """

    placeholder_version: int | MISSING = MISSING
    """
    Version of the placeholder.
    """

    description: str | MISSING = MISSING
    """
    Alt text of the image.
    """

    flags: bitfields.EmbedMediaFlags | MISSING = MISSING
    """
    Embed media flags combined as a bitfield.
    """

    _transforms: ClassVar[dict] = {
        "flags": bitfields.EmbedMediaFlags,
    }
