"""
Discord API bitfield flags module.
"""

from .application import ApplicationFlags
from .attachment import AttachmentFlags
from .channel import ChannelFlags
from .embed import EmbedFlags, EmbedMediaFlags
from .guild import SystemChannelFlags
from .member import MemberFlags
from .message import MessageFlags
from .role import RoleFlags
from .user import UserFlags

__all__ = [
    "ApplicationFlags",
    "AttachmentFlags",
    "ChannelFlags",
    "EmbedFlags",
    "EmbedMediaFlags",
    "MemberFlags",
    "MessageFlags",
    "RoleFlags",
    "SystemChannelFlags",
    "UserFlags",
]
