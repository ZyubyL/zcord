from enum import StrEnum


class WebhookEventType(StrEnum):
    """Webhook event types an application can subscribe to."""

    APPLICATION_AUTHORIZED = "APPLICATION_AUTHORIZED"
    """Sent when an app was authorized by a user to a server or their \
    account."""

    APPLICATION_DEAUTHORIZED = "APPLICATION_DEAUTHORIZED"
    """Sent when an app was deauthorized by a user."""

    ENTITLEMENT_CREATE = "ENTITLEMENT_CREATE"
    """Entitlement was created."""

    ENTITLEMENT_UPDATE = "ENTITLEMENT_UPDATE"
    """Entitlement was updated."""

    ENTITLEMENT_DELETE = "ENTITLEMENT_DELETE"
    """Entitlement was deleted."""

    QUEST_USER_ENROLLMENT = "QUEST_USER_ENROLLMENT"
    """User was added to a quest.

    Notes:
        Currently unavailable.
    """

    LOBBY_MESSAGE_CREATE = "LOBBY_MESSAGE_CREATE"
    """Sent when a message is created in a lobby."""

    LOBBY_MESSAGE_UPDATE = "LOBBY_MESSAGE_UPDATE"
    """Sent when a message is updated in a lobby."""

    LOBBY_MESSAGE_DELETE = "LOBBY_MESSAGE_DELETE"
    """Sent when a message is deleted in a lobby."""

    GAME_DIRECT_MESSAGE_CREATE = "GAME_DIRECT_MESSAGE_CREATE"
    """Sent when a direct message is created during an active Social SDK \
    session."""

    GAME_DIRECT_MESSAGE_UPDATE = "GAME_DIRECT_MESSAGE_UPDATE"
    """Sent when a direct message is updated during an active Social SDK \
    session."""

    GAME_DIRECT_MESSAGE_DELETE = "GAME_DIRECT_MESSAGE_DELETE"
    """Sent when a direct message is deleted during an active Social SDK \
    session."""
