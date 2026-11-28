"""Discord API bitfield flags module."""

from zcord.api.application.bitfields import ApplicationFlags
from zcord.api.channel.bitfields import ChannelFlags
from zcord.api.guild.bitfields import GuildMemberFlags, SystemChannelFlags
from zcord.api.invite.bitfields import GuildInviteFlags
from zcord.api.lobby.bitfields import LobbyMemberFlags
from zcord.api.message.bitfields import (
    AttachmentFlags,
    EmbedFlags,
    EmbedMediaFlags,
    MessageFlags,
)
from zcord.api.permissons.bitfields import RoleFlags
from zcord.api.sku.bitfields import SkuFlags
from zcord.api.user.bitfields import UserFlags

from .activity import ActivityFlags
from .intents import Intents

__all__ = [
    "ActivityFlags",
    "ApplicationFlags",
    "AttachmentFlags",
    "ChannelFlags",
    "EmbedFlags",
    "EmbedMediaFlags",
    "GuildInviteFlags",
    "GuildMemberFlags",
    "Intents",
    "LobbyMemberFlags",
    "MessageFlags",
    "RoleFlags",
    "SkuFlags",
    "SystemChannelFlags",
    "UserFlags",
]
