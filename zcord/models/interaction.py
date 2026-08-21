from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar

from zcord.enums.interaction import InteractionType
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.channel import Channel
from zcord.models.guild import Guild
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.message import Message


@dataclass(frozen=True, slots=True)
class InteractionMetadata(Model):
    """
    Contain metadata about the [`Interaction`][zcord.Interaction].

    Attributes:
        id:
            The ID of the interaction.
        type:
            The type of the interaction.
        user:
            The user who triggered the interaction.
        authorizing_integration_owners:
            A dictionary for authorizing integeration owners.
        original_response_message_id:
            The ID of the original response message, only present on follow-up.
        target_user:
            The user the command was run on.
        target_message_id:
            The ID of the message the command was run on.
        interacted_message_id:
            The ID of the message that contained the interacted component.
        triggering_interaction_metadata:
            Metadata for the interaction that was used to open the modal.
    """

    id: Snowflake
    type: InteractionType
    user: User
    authorizing_integration_owners: dict
    original_response_message_id: Snowflake | MISSING = MISSING
    target_user: User | MISSING = MISSING
    target_message_id: Snowflake | MISSING = MISSING
    interacted_message_id: Snowflake | MISSING = MISSING
    triggering_interaction_metadata: InteractionMetadata | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": InteractionType,
        "user": User,
        "original_response_message_id": Snowflake,
        "target_user": User,
        "target_message_id": Snowflake,
        "interacted_message_id": Snowflake,
    }


InteractionMetadata._transforms["triggering_interaction_metadata"] = (
    InteractionMetadata
)


@dataclass(frozen=True, slots=True)
class Interaction(Model):
    """
    Represent a Discord interaction.

    Attributes:
        id:
            The ID of the interaction.
        application_id:
            The ID of the application this interaction is for.
        type:
            The type of interaction.
        data:
            Interaction data.
        guild:
            The guild this interaction was sent from.
        guild_id:
            The guild ID this interaction was sent from.
        channel:
            The channel this interaction was sent from.
        channel_id:
            The channel ID this interaction was sent from.
        member:
            The guild member who invoked the interaction.
        user:
            The user who invoked the interaction.
        token:
            Continuation token for responding to the interaction.
        message:
            The message attached to this interaction.
        app_permissions:
            Bitwise set of permissions the app has in the source location of \
            the interaction.
        locale:
            Selected language of the invoking user.
        guild_locale:
            The guild's preferred locale.
        entitlements:
            List of entitlements for monetized apps.
        authorizing_integration_owners:
            A dictionary for authorizing integeration owners.
        context:
            The context where the interaction was triggered from.
        attachment_size_limit:
            Attachment size limit in bytes.
    """

    id: Snowflake
    application_id: Snowflake
    type: InteractionType
    token: str
    entitlements: list
    authorizing_integration_owners: dict
    attachment_size_limit: int
    data: Any | MISSING = MISSING
    guild: Guild | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    channel: Channel | MISSING = MISSING
    channel_id: Snowflake | MISSING = MISSING
    member: Any | MISSING = MISSING
    user: User | MISSING = MISSING
    message: Message | MISSING = MISSING
    app_permissions: str | MISSING = MISSING
    locale: str | MISSING = MISSING
    guild_locale: str | MISSING = MISSING
    context: Any | MISSING = MISSING

    from zcord.models.message import Message

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "application_id": Snowflake,
        "type": InteractionType,
        "guild": Guild,
        "guild_id": Snowflake,
        "channel": Channel,
        "channel_id": Snowflake,
        "user": User,
        "message": Message,
    }
