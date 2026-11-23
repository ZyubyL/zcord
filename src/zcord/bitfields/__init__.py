"""Discord API bitfield flags module."""

from .activity import ActivityFlags
from .application import ApplicationFlags
from .attachment import AttachmentFlags
from .channel import ChannelFlags
from .embed import EmbedFlags, EmbedMediaFlags
from .guild import SystemChannelFlags
from .intents import Intents
from .member import GuildMemberFlags, MemberFlags
from .message import MessageFlags
from .role import RoleFlags
from .user import UserFlags

__all__ = [
    "ActivityFlags",
    "ApplicationFlags",
    "AttachmentFlags",
    "ChannelFlags",
    "EmbedFlags",
    "EmbedMediaFlags",
    "GuildMemberFlags",
    "Intents",
    "MemberFlags",
    "MessageFlags",
    "RoleFlags",
    "SystemChannelFlags",
    "UserFlags",
]
