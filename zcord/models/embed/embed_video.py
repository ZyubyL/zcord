from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedVideo(Model):
    """
    Contain embed's video info.
    """

    url: str | MISSING = MISSING
    """
    Source URL of the video.
    """

    proxy_url: str | MISSING = MISSING
    """
    A proxied URL of the video.
    """

    height: int | MISSING = MISSING
    """
    The video's height.
    """

    width: int | MISSING = MISSING
    """
    The video's width.
    """

    content_type: str | MISSING = MISSING
    """
    The video's media type.
    """

    placeholder: str | MISSING = MISSING
    """
    Thumbhash placeholder of the video.
    """

    placeholder_version: int | MISSING = MISSING
    """
    Version of the placeholder.
    """

    description: str | MISSING = MISSING
    """
    Alt text of the video.
    """

    flags: bitfields.EmbedMediaFlags | MISSING = MISSING
    """
    Embed media flags combined as a bitfield.
    """

    _transforms: ClassVar[dict] = {
        "flags": bitfields.EmbedMediaFlags,
    }
