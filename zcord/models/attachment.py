from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.flags import AttachmentFlags
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Attachment(ZcordModel):
    """
    Represent a Discord attachment.

    Attributes:
        id:
            The ID of the attachment.
        filename:
            The name of the file attached.
        title:
            The title of the file.
        description:
            Alt text for the file.
        content_type:
            The media type of the attachment.
        size:
            The size of the attachment.
        url:
            The source url of the file.
        proxy_url:
            A proxied url of the file.
        height:
            The height of the image/video file.
        width:
            The width of the image/video file.
        placeholder:
            Thumbhash placeholder for image/video file.
        placeholder_version:
            Version of the image/video file.
        ephemeral:
            Whether this attachment is ephemeral.
        duration_secs:
            The duration of the audio/video file.
        waveform:
            Base64 encoded bytearray represent a sampled waveform for voice \
            messages.
        flags:
            The attachment flags combined as a bitfield.
        clip_participants:
            A list of users who were in the stream when it is clipped.
        clip_created_at:
            The timestamp for when the clip is created.
        application:
            The application in the stream, if recognized, when it is clipped.
    """

    id: Snowflake
    filename: str
    size: int
    url: str
    proxy_url: str
    title: str | MISSING = MISSING
    description: str | MISSING = MISSING
    content_type: str | MISSING = MISSING
    height: int | None | MISSING = MISSING
    width: int | None | MISSING = MISSING
    placeholder: str | MISSING = MISSING
    placeholder_version: int | MISSING = MISSING
    ephemeral: bool | MISSING = MISSING
    duration_secs: float | MISSING = MISSING
    waveform: str | MISSING = MISSING
    flags: AttachmentFlags | MISSING = MISSING
    clip_participants: list[User] | MISSING = MISSING
    clip_created_at: datetime | MISSING = MISSING
    application: Any | None | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "flags": AttachmentFlags,
        "clip_participants": User,
        "clip_created_at": datetime.fromisoformat,
    }
