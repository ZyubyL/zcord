from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.application import Application
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Attachment(Model):
    """
    Represent a Discord attachment.
    """

    id: Snowflake
    """
    The ID of the attachment.
    """

    filename: str
    """
    The name of the file attached.
    """

    size: int
    """
    The size of the attachment.
    """

    url: str
    """
    The source url of the file.
    """

    proxy_url: str
    """
    A proxied url of the file.
    """

    title: str | MISSING = MISSING
    """
    The title of the file.
    """

    description: str | MISSING = MISSING
    """
    Alt text for the file.
    """

    content_type: str | MISSING = MISSING
    """
    The media type of the attachment.
    """

    height: int | None | MISSING = MISSING
    """
    The height of the image/video file.
    """

    width: int | None | MISSING = MISSING
    """
    The width of the image/video file.
    """

    placeholder: str | MISSING = MISSING
    """
    Thumbhash placeholder for image/video file.
    """

    placeholder_version: int | MISSING = MISSING
    """
    Version of the image/video file.
    """

    ephemeral: bool | MISSING = MISSING
    """
    Whether this attachment is ephemeral.
    """

    duration_secs: float | MISSING = MISSING
    """
    The duration of the audio/video file.
    """

    waveform: str | MISSING = MISSING
    """
    Base64 encoded bytearray represent a sampled waveform for voice messages.
    """

    flags: bitfields.AttachmentFlags | MISSING = MISSING
    """
    The attachment flags combined as a bitfield.
    """

    clip_participants: tuple[User] | MISSING = MISSING
    """
    A list of users who were in the stream when it is clipped.
    """

    clip_created_at: datetime | MISSING = MISSING
    """
    The timestamp for when the clip is created.
    """

    application: Application | None | MISSING = MISSING
    """
    The application in the stream, if recognized, when it is clipped.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "flags": bitfields.AttachmentFlags,
        "clip_participants": User,
        "clip_created_at": datetime.fromisoformat,
        "application": Application,
    }
