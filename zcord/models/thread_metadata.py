from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ThreadMetadata(Model):
    """
    Contain thread specific data.
    """

    archived: bool
    """
    Whether the thread is archived.
    """

    auto_archive_duration: int
    """
    The duration in minutes after which the thread is automatically archived.
    """

    archive_timestamp: datetime
    """
    The timestamp when the thread was archived.
    """

    locked: bool
    """
    Whether the thread is locked.[^1]

    [^1]: When the thread is locked, only users with `MANAGE_THREADS` \
    permission can unarchive it.
    """

    invitable: bool | MISSING = MISSING
    """
    Whether non-moderators can add other non-moderators to the thread.
    """

    create_timestamp: datetime | None | MISSING = MISSING
    """
    The timestamp when the thread was created.[^1]

    [^1]: Only populated for threads created after January 1, 2022.
    """

    _transforms: ClassVar[dict] = {
        "archive_timestamp": datetime.fromtimestamp,
        "create_timestamp": datetime.fromtimestamp,
    }
