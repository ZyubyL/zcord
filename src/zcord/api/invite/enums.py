from enum import IntEnum


class InviteTargetType(IntEnum):
    STREAM = 1
    EMBEDDED_APPLICATION = 2


class InviteType(IntEnum):
    GUILD = 0
    GROUP_DM = 1
    FRIEND = 2
