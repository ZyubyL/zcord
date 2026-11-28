from enum import IntFlag


class MessageFlags(IntFlag):
    CROSSPOSTED = 1 << 0
    """This message has been published to subscribed channels \
    (via Channel Following)."""

    IS_CROSSPOST = 1 << 1
    """This message originated from a message in another channel \
    (via Channel Following)."""

    SUPPRESS_EMBEDS = 1 << 2
    """Do not include any embeds when serializing this message."""

    SOURCE_MESSAGE_DELETED = 1 << 3
    """The source message for this crosspost has been deleted \
    (via Channel Following)."""

    URGENT = 1 << 4
    """This message came from the urgent message system."""

    HAS_THREAD = 1 << 5
    """This message has an associated thread, \
    with the same id as the message."""

    EPHEMERAL = 1 << 6
    """This message is only visible to the user who invoked the Interaction."""

    LOADING = 1 << 7
    """This message is an Interaction Response and the bot is "thinking"."""

    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    """This message failed to mention some roles \
    and add their members to the thread."""

    SUPPRESS_NOTIFICATIONS = 1 << 12
    """This message will not trigger push and desktop notifications."""

    IS_VOICE_MESSAGE = 1 << 13
    """This message is a voice message."""

    HAS_SNAPSHOT = 1 << 14
    """This message has a snapshot (via Message Forwarding)."""

    IS_COMPONENTS_V2 = 1 << 15
    """Allows you to create fully component-driven messages."""

    _SEND_MESSAGE_FLAGS = (
        SUPPRESS_EMBEDS
        | SUPPRESS_NOTIFICATIONS
        | IS_VOICE_MESSAGE
        | IS_COMPONENTS_V2
    )


class EmbedFlags(IntFlag):
    CONTAINS_EXPLICIT_CONTENT = 1 << 4
    """This embed's media was flagged as explicit \
    by Discord's content scanning."""

    IS_CONTENT_INVENTORY_ENTRY = 1 << 5
    """This embed is a fallback for a reply to an activity card."""

    CONTAINS_GORE_CONTENT = 1 << 6
    """This embed's media was flagged as gore by Discord's content scanning."""

    CONTAINS_SELF_HARM_CONTENT = 1 << 7
    """This embed's media was flagged as self-harm \
    by Discord's content scanning."""


class EmbedMediaFlags(IntFlag):
    IS_ANIMATED = 1 << 5
    """This image is animated."""


class AttachmentFlags(IntFlag):
    IS_CLIP = 1 << 0
    """This attachment is a Clip from a stream."""

    IS_THUMBNAIL = 1 << 1
    """This attachment is the thumbnail of a thread in a media channel, \
    displayed in the grid but not on the message."""

    IS_SPOILER = 1 << 3
    """This attachment was marked as a spoiler and is blurred until clicked."""

    CONTAINS_EXPLICIT_CONTENT = 1 << 4
    """This attachment was flagged as explicit by Discord's content scanning."""

    IS_ANIMATED = 1 << 5
    """This attachment is an animated image."""

    CONTAINS_GORE_CONTENT = 1 << 6
    """This attachment was flagged as gore by Discord's content scanning."""

    CONTAINS_SELF_HARM_CONTENT = 1 << 7
    """This attachment was flagged as self-harm \
    by Discord's content scanning."""
