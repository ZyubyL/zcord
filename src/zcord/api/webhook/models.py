from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord import enums
from zcord.api.channel.models import Channel
from zcord.api.guild.models import Guild
from zcord.api.model import Model
from zcord.api.user.models import User
from zcord.missing import MISSING
from zcord.snowflake import Snowflake


@dataclass(frozen=True, slots=True)
class Webhook(Model):
    id: Snowflake
    """The ID of the webhook."""

    type: enums.WebhookType
    """The type of the webhook."""

    guild_id: Snowflake | None | MISSING = MISSING
    """The guild id this webhook is for, if any."""

    channel_id: Snowflake | None = None
    """The channel id this webhook is for, if any."""

    user: User | MISSING = MISSING
    """The user this webhook was created by \
    (not returned when getting a webhook with its token)."""

    name: str | None = None
    """The default name of the webhook."""

    avatar: str | None = None
    """The default user avatar hash of the webhook."""

    token: str | MISSING = MISSING
    """The secure token of the webhook (returned for Incoming Webhooks)."""

    application_id: Snowflake | None = None
    """The bot/OAuth2 application that created this webhook."""

    source_guild: Guild | MISSING = MISSING
    """The guild of the channel that this webhook is following \
    (returned for Channel Follower Webhooks)."""

    source_channel: Channel | MISSING = MISSING
    """The channel that this webhook is following \
    (returned for Channel Follower Webhooks)."""

    url: str | MISSING = MISSING
    """The url used for executing the webhook \
    (returned by the webhooks OAuth2 flow)."""

    _transforms: ClassVar[dict[str, Any]] = {
        "id": Snowflake,
        "type": enums.WebhookType,
        "guild_id": Snowflake,
        "channel_id": Snowflake,
        "user": User,
        "application_id": Snowflake,
        "source_guild": Guild,
        "source_channel": Channel,
    }
