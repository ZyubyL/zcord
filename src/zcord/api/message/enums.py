from enum import IntEnum, StrEnum


class MessageType(IntEnum):
    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44
    POLL_RESULT = 46


class MessageActivityType(IntEnum):
    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5
    STREAM_REQUEST = 6


class MessageReferenceType(IntEnum):
    DEFAULT = 0
    """A standard reference used by replies."""

    FORWARD = 1
    """Reference used to point to a message at a point in time."""


class EmbedType(StrEnum):
    RICH = "rich"
    """Generic embed rendered from embed attributes."""

    IMAGE = "image"
    """Image embed."""

    VIDEO = "video"
    """Video embed."""

    AUDIO = "audio"
    """Audio embed rendered with an inline audio player."""

    GIFV = "gifv"
    """Animated gif image embed rendered as a video embed."""

    ARTICLE = "article"
    """Article embed."""

    LINK = "link"
    """Link embed."""

    POLL_RESULT = "poll_result"
    """Poll result embed."""

    COMPONENT = "components"
    """Link preview built from Discord components."""


class BaseTheme(IntEnum):
    UNSET = 0
    """Equivalent to `DARK`."""

    DARK = 1
    LIGHT = 2
    DARKER = 3
    MIDNIGHT = 4
