from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, ClassVar, Literal

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild.integration_account import IntegrationAccount
from zcord.models.guild.integration_application import IntegrationApplication
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Integration(Model):
    id: Snowflake
    """Integration ID."""

    name: str
    """Integration name."""

    type: Literal["twitch", "youtube", "discord", "guild_subscription"]
    """Integration type."""

    enabled: bool
    """Is this integration enabled."""

    account: IntegrationAccount
    """Integration account information."""

    syncing: bool | MISSING = MISSING
    """Is this integration syncing."""

    role_id: Snowflake | MISSING = MISSING
    """ID that this integration uses for "subscribers"."""

    enable_emoticons: bool | MISSING = MISSING
    """Whether emoticons should be synced for this integration."""

    expire_behavior: enums.IntegrationExpireBehavior | MISSING = MISSING
    """The behavior of expiring subscribers."""

    expire_grace_period: int | MISSING = MISSING
    """The grace period (in days) before expiring subscribers."""

    user: User | MISSING = MISSING
    """User for this integration."""

    synced_at: datetime | MISSING = MISSING
    """When this integration was last synced."""

    subscriber_count: int | MISSING = MISSING
    """How many subscribers this integration has."""

    revoked: bool | MISSING = MISSING
    """Has this integration been revoked."""

    application: IntegrationApplication | MISSING = MISSING
    """The bot/OAuth2 appliction for Discord integration."""

    scopes: tuple[OAuth2Scope, ...] | MISSING = MISSING
    """The scopes the application has been authorized for."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "account": IntegrationAccount,
        "role_id": Snowflake,
        "expire_behavior": enums.IntegrationExpireBehavior,
        "user": User,
        "synced_at": datetime.fromisoformat,
        "application": IntegrationApplication,
        "scopes": OAuth2Scope,
    }
