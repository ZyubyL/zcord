from __future__ import annotations

from enum import IntFlag


class MemberFlags(IntFlag):
    """
    | Flag | Value | Description |
    |------|-------|-------------|
    | `DID_REJOIN` | `1 << 0` | Member has left and rejoin the guild. |
    | `COMPLETED_ONBOARDING` | `1 << 1` | Member has completed the onboarding \
    process. |
    | `BYPASSED_VERIFICATION` | `1 << 2` | Member is excempt from guild \
    verification. |
    | `STARTED_ONBOARDING` | `1 << 3` | Member has started the onboarding \
    process. |
    | `IS_GUEST` | `1 << 4` | Member is a guest and can only access the \
    invited voice channel. |
    | `STARTED_HOME_ACTIONS` | `1 << 5` | Member has started the Server Guide \
    new member actions. |
    | `COMPLETED_HOME_ACTIONS` | `1 << 6` | Member has completed the \
    Server Guide new member actions. |
    | `AUTOMOD_QUARANTINED_USERNAME` | `1 << 7` | Member has been quarantined \
    by the automod system because of their username, display name or nickname. |
    | `DM_SETTINGS_UPSELL_ACKNOWLEDGED` | `1 << 9` | Member has dismissed the \
    DM settings upsell. |
    | `AUTOMOD_QUARANTINED_GUILD_TAG` | `1 << 10` | Member has been \
    quarantined by the automod system because of their guild tag. |
    """

    DID_REJOIN = 1 << 0
    COMPLETED_ONBOARDING = 1 << 1
    BYPASSES_VERIFICATION = 1 << 2
    STARTED_ONBOARDING = 1 << 3
    IS_GUEST = 1 << 4
    STARTED_HOME_ACTIONS = 1 << 5
    COMPLETED_HOME_ACTIONS = 1 << 6
    AUTOMOD_QUARANTINED_USERNAME = 1 << 7
    DM_SETTINGS_UPSELL_ACKNOWLEDGED = 1 << 9
    AUTOMOD_QUARANTINED_GUILD_TAG = 1 << 10
