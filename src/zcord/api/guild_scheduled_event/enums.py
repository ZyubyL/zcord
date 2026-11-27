from enum import IntEnum


class PrivacyLevel(IntEnum):
    GUILD_ONLY = 2
    """The scheduled event is only accessible to guild members."""


class ScheduledEntityType(IntEnum):
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3


class ScheduledEventRecurrenceRuleFrequency(IntEnum):
    YEARLY = 0
    MONTHLY = 1
    WEEKLY = 2
    DAILY = 3


class ScheduledEventRecurrenceRuleMonth(IntEnum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class ScheduledEventRecurrenceRuleWeekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class ScheduledEventStatus(IntEnum):
    """Once is set to COMPLETED or CANCELED, it can no longer be updated."""

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4
