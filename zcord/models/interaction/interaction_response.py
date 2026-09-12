from __future__ import annotations

from typing import TYPE_CHECKING

from zcord import enums
from zcord._builders.interaction_callback import _InteractionCallback

if TYPE_CHECKING:
    from zcord.models.message import Message
    from zcord.models.snowflake import Snowflake
    from zcord.state import ConnectionState


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
