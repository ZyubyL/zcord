from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import bitfields, cdn, enums, types
from zcord.api.channel.models import Channel
from zcord.api.entitlement.models import Entitlement
from zcord.api.guild.models import Guild, GuildMember
from zcord.api.message.models import Message
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Interaction(Model):
    id: Snowflake
    """ID of the interaction."""

    application_id: Snowflake
    """ID of the application this interaction is for."""

    type: enums.InteractionType
    """Type of interaction."""

    token: str
    """Continuation token for responding to the interaction."""

    version: int
    """Read-only property, always `1`."""

    app_permissions: bitfields.Permission
    """Bitwise set of permissions the app has in the source location \
    of the interaction."""

    entitlements: tuple[Entitlement, ...]
    """For monetized apps, any entitlements for the invoking user, \
    representing access to premium SKUs."""

    authorizing_integration_owners: dict[enums.ApplicationIntegrationType, Any]
    """Mapping of installation contexts that the interaction was authorized \
    for to related user or guild IDs."""

    attachment_size_limit: int
    """Attachment size limit in bytes."""

    data: InteractionData | MISSING = MISSING
    """Interaction data payload."""

    guild: Guild | MISSING = MISSING
    """Guild that the interaction was sent from."""

    guild_id: Snowflake | MISSING = MISSING
    """Guild that the interaction was sent from."""

    channel: Channel | MISSING = MISSING
    """Channel that the interaction was sent from."""

    channel_id: Snowflake | MISSING = MISSING
    """Channel that the interaction was sent from."""

    member: GuildMember | MISSING = MISSING
    """Guild member data for the invoking user, including permissions."""

    user: User | MISSING = MISSING
    """User object for the invoking user, if invoked in a DM."""

    message: Message | MISSING = MISSING
    """For components or modals triggered by components, \
    the message they were attached to."""

    locale: str | MISSING = MISSING
    """Selected language of the invoking user."""

    guild_locale: str | MISSING = MISSING
    """Guild's preferred locale, if invoked in a guild."""

    context: enums.InteractionContextType | MISSING = MISSING
    """Context where the interaction was triggered from."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "application_id": Snowflake,
        "type": enums.InteractionType,
        "data": InteractionData,
        "guild": Guild,
        "guild_id": Snowflake,
        "channel": Channel,
        "channel_id": Snowflake,
        "member": GuildMember,
        "user": User,
        "message": Message,
        "app_permissions": bitfields.Permission,
        "entitlements": Entitlement,
        "context": enums.InteractionContextType,
    }
