from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.channel import Channel
from zcord.models.guild import Guild
from zcord.models.member import Member
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.message import Message


@dataclass(frozen=True, slots=True)
class InteractionMetadata(Model):
    """
    Contain metadata about the [`Interaction`][zcord.Interaction].
    """

    id: Snowflake
    """
    The ID of the interaction.
    """

    type: enums.InteractionType
    """
    The type of the interaction.
    """

    user: User
    """
    The user who triggered the interaction.
    """

    authorizing_integration_owners: dict
    """
    A dictionary for authorizing integeration owners.
    """

    original_response_message_id: Snowflake | MISSING = MISSING
    """
    The ID of the original response message, only present on follow-up.
    """

    target_user: User | MISSING = MISSING
    """
    The user the command was run on.
    """

    target_message_id: Snowflake | MISSING = MISSING
    """
    The ID of the message the command was run on.
    """

    interacted_message_id: Snowflake | MISSING = MISSING
    """
    The ID of the message that contained the interacted component.
    """

    triggering_interaction_metadata: InteractionMetadata | MISSING = MISSING
    """
    Metadata for the interaction that was used to open the modal.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "type": enums.InteractionType,
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
    """

    id: Snowflake
    """
    The ID of the interaction.
    """

    application_id: Snowflake
    """
    The ID of the application this interaction is for.
    """

    type: enums.InteractionType
    """
    The type of interaction.
    """

    token: str
    """
    Continuation token for responding to the interaction.
    """

    entitlements: list
    """
    List of entitlements for monetized apps.
    """

    authorizing_integration_owners: dict
    """
    A dictionary for authorizing integeration owners.
    """

    attachment_size_limit: int
    """
    Attachment size limit in bytes.
    """

    data: Any | MISSING = MISSING
    """
    Interaction data.
    """

    guild: Guild | MISSING = MISSING
    """
    The guild this interaction was sent from.
    """

    guild_id: Snowflake | MISSING = MISSING
    """
    The guild ID this interaction was sent from.
    """

    channel: Channel | MISSING = MISSING
    """
    The channel this interaction was sent from.
    """

    channel_id: Snowflake | MISSING = MISSING
    """
    The channel ID this interaction was sent from.
    """

    member: Member | MISSING = MISSING
    """
    The guild member who invoked the interaction.
    """

    user: User | MISSING = MISSING
    """
    The user who invoked the interaction.
    """

    message: Message | MISSING = MISSING
    """
    The message attached to this interaction.
    """

    app_permissions: str | MISSING = MISSING
    """
    Bitwise set of permissions the app has in the source location of \
    the interaction.
    """

    locale: str | MISSING = MISSING
    """
    Selected language of the invoking user.
    """

    guild_locale: str | MISSING = MISSING
    """
    The guild's preferred locale.
    """

    context: enums.InteractionContextType | MISSING = MISSING
    """
    The context where the interaction was triggered from.
    """

    from zcord.models.message import Message

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "application_id": Snowflake,
        "type": enums.InteractionType,
        "guild": Guild,
        "guild_id": Snowflake,
        "channel": Channel,
        "channel_id": Snowflake,
        "user": User,
        "message": Message,
        "member": Member,
    }


@dataclass(frozen=True, slots=True)
class InteractionResponse(Model):
    type: enums.InteractionCallbackType
    data: Any | MISSING = MISSING
