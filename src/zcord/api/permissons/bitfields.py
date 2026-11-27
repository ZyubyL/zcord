from enum import IntFlag


class RoleFlags(IntFlag):
    NONE = 0
    IN_PROMPT = 1 << 0
