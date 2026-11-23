from enum import IntEnum


class MembershipState(IntEnum):
    """User's membership state on the team."""

    INVITED = 1
    ACCEPTED = 2
