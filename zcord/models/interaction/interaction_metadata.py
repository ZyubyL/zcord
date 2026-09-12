from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


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
