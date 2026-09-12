from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING, Any, ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.channel import Channel
from zcord.models.guild import Guild
from zcord.models.interaction.interaction_data.base import InteractionData
from zcord.models.interaction.interaction_response import InteractionResponse
from zcord.models.member import Member
from zcord.models.snowflake import Snowflake
from zcord.models.user import User

if TYPE_CHECKING:
    from zcord.models.message import Message
    from zcord.state import ConnectionState


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
