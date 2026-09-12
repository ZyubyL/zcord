from __future__ import annotations

from dataclasses import dataclass, replace
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
    from zcord.state import ConnectionState


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
    A dictionary for authorizing integration owners.
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


class InteractionData(Model):
    """
    Base class for interaction data payloads.
    """

    _registry: ClassVar[dict[enums.InteractionType, type[InteractionData]]] = {}


@dataclass(frozen=True, slots=True)
class ComponentInteractionData(InteractionData):
    """
    Data for a \
    [`MESSAGE_COMPONENT`][zcord.enums.InteractionType.MESSAGE_COMPONENT] \
    interaction.
    """

    custom_id: str
    """
    The custom ID of the component.
    """

    component_type: enums.ComponentType
    """
    The type of the component.
    """

    values: tuple[str, ...] | MISSING = MISSING
    """
    The values selected in a select menu component.
    """

    _transforms: ClassVar[dict] = {
        "component_type": enums.ComponentType,
    }


@dataclass(frozen=True, slots=True)
class ApplicationCommandInteractionData(InteractionData):
    """
    Data for an \
    [`APPLICATION_COMMAND`][zcord.enums.InteractionType.APPLICATION_COMMAND] \
    interaction.
    """

    id: Snowflake
    """
    The ID of the invoked command.
    """

    name: str
    """
    The name of the invoked command.
    """

    type: int
    """
    The type of the invoked command.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
    }


@dataclass(frozen=True, slots=True)
class ModalSubmitInteractionData(InteractionData):
    """
    Data for a [`MODAL_SUBMIT`][zcord.enums.InteractionType.MODAL_SUBMIT] \
    interaction.
    """

    custom_id: str
    """
    The custom ID of the modal.
    """

    components: tuple[Any, ...] = ()
    """
    The components submitted with the modal.
    """


_ACID = ApplicationCommandInteractionData

InteractionData._registry = {
    enums.InteractionType.MESSAGE_COMPONENT: ComponentInteractionData,
    enums.InteractionType.APPLICATION_COMMAND: _ACID,
    enums.InteractionType.APPLICATION_COMMAND_AUTOCOMPLETE: _ACID,
    enums.InteractionType.MODAL_SUBMIT: ModalSubmitInteractionData,
}


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
    A dictionary for authorizing integration owners.
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

    _state: ClassVar[ConnectionState | MISSING] = MISSING

    @classmethod
    def _from_payload(cls, payload):
        obj = Model._from_payload.__func__(cls, payload)
        data = payload.get("data")
        if data and isinstance(data, dict):
            itype = payload.get("type")
            data_cls = InteractionData._registry.get(itype)
            if data_cls:
                return replace(
                    obj,
                    data=data_cls._from_payload(data),
                )
        return obj

    @property
    def respond(self) -> InteractionResponse:
        """
        Get an interface for responding to this interaction.
        """
        assert self._state is not MISSING
        return InteractionResponse(
            state=self._state,
            interaction_id=self.id,
            interaction_token=self.token,
        )


@dataclass(frozen=True, slots=True)
class _InteractionCallback(Model):
    type: enums.InteractionCallbackType
    data: Any | MISSING = MISSING


class InteractionResponse:
    """
    Interface for responding to an \
    [`Interaction`][zcord.Interaction].
    """

    def __init__(
        self,
        state: ConnectionState,
        interaction_id: Snowflake,
        interaction_token: str,
    ) -> None:
        self._state = state
        self._interaction_id = interaction_id
        self._interaction_token = interaction_token

    async def send(self, message: Message) -> Message:
        """
        Respond to the interaction with a new message.

        Returns:
            The created message.

        Raises:
            errors.HTTPError:
                The request failed.
        """
        msg = await self._state.create_interaction_response(
            interaction_id=self._interaction_id,
            interaction_token=self._interaction_token,
            callback=_InteractionCallback(
                type=enums.InteractionCallbackType.CHANNEL_MESSAGE_WITH_SOURCE,
                data=message._to_payload(),
            ),
            with_response=True,
        )
        assert msg is not None
        return msg

    async def defer(self) -> None:
        """
        ACK the interaction without showing a loading state.

        Use this to defer the response and edit the original \
        message later.

        Raises:
            errors.HTTPError:
                The request failed.
        """
        await self._state.create_interaction_response(
            interaction_id=self._interaction_id,
            interaction_token=self._interaction_token,
            callback=_InteractionCallback(
                type=enums.InteractionCallbackType.DEFERRED_UPDATE_MESSAGE,
            ),
        )

    async def edit(self, message: Message) -> Message:
        """
        Edit the message the component was attached to.

        Returns:
            The edited message.

        Raises:
            errors.HTTPError:
                The request failed.
        """
        msg = await self._state.create_interaction_response(
            interaction_id=self._interaction_id,
            interaction_token=self._interaction_token,
            callback=_InteractionCallback(
                type=enums.InteractionCallbackType.UPDATE_MESSAGE,
                data=message._to_payload(),
            ),
            with_response=True,
        )
        assert msg is not None
        return msg
