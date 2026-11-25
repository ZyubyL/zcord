from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class ThreadMetadata(Model):
    archived: bool
    """Whether the thread is archived."""

    auto_archive_duration: int
    """The thread will stop showing in the channel list after \
    this many minutes of inactivity.

    Notes:
        Can be set to `60`, `1440`, `4320`, `10080`.
    """

    archive_timestamp: datetime
    """Timestamp when the thread's archive status was last changed, \
    used for calculating recent activity."""

    locked: bool
    """Whether the thread is locked, only users with `MANAGE_THREADS` can \
    unarchive it."""

    invitable: bool | MISSING = MISSING
    """Whether non-moderators can add other non-moderators to a thread.
    Only available on private threads."""

    create_timestamp: datetime | None | MISSING = MISSING
    """Timestamp when the thread was created.

    Notes:
        This field is only in threads created before 2022/01/09.
    """

    _transforms: ClassVar[dict[str, Any]] = {
        "archive_timestamp": datetime.fromisoformat,
        "create_timestamp": datetime.fromisoformat,
    }
