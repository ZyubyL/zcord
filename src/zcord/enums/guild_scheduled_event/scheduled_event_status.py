from enum import IntEnum


class ScheduledEventStatus(IntEnum):
    """Once is set to COMPLETED or CANCELED, it can no longer be updated."""

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4
