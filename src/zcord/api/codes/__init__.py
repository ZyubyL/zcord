"""Read more at https://docs.discord.com/developers/topics/opcodes-and-status-codes"""

from .enums import (
    GatewayCloseEventCode,
    GatewayOpCode,
    RpcCloseEventCode,
    RpcErrorCode,
    VoiceCloseEventCode,
    VoiceOpcode,
)

__all__ = [
    "GatewayCloseEventCode",
    "GatewayOpCode",
    "RpcCloseEventCode",
    "RpcErrorCode",
    "VoiceCloseEventCode",
    "VoiceOpcode",
]
