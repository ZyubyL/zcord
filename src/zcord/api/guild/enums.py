from enum import IntEnum


class AgeRestrictionLevel(IntEnum):
    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class DefaultMessageNotificationLevel(IntEnum):
    ALL_MESSAGES = 0
    """Members will receive notifications for all messages by default."""

    ONLY_MENTIONS = 1
    """Members will receive notifications only for messages that @mention them \
    by default."""


class ExplicitContentFilterLevel(IntEnum):
    DISABLED = 0
    """Media content will not be scanned."""

    MEMBERS_WITHOUT_ROLES = 1
    """Media content sent by members without roles will be scanned."""

    ALL_MEMBERS = 2
    """Media content sent by all members will be scanned."""


class IntegrationExpireBehavior(IntEnum):
    REMOVE_ROLE = 0
    KICK = 1


class MFALevel(IntEnum):
    NONE = 0
    """Guild has no MFA/2FA requirement for moderation actions."""

    ELEVATED = 1
    """Guild has 2FA requirement for moderation actions."""


class PremiumTier(IntEnum):
    NONE = 0
    """Guild has not unlocked any Server Boost perks."""

    TIER_1 = 1
    """Guild has unlocked Server Boost level 1 perks."""

    TIER_2 = 2
    """Guild has unlocked Server Boost level 2 perks."""

    TIER_3 = 3
    """Guild has unlocked Server Boost level 3 perks."""


class VerificationLevel(IntEnum):
    NONE = 0
    """Unrestricted."""

    LOW = 1
    """Must have verified email on account."""

    MEDIUM = 2
    """Must be registered on Discord for longer than 5 minutes."""

    HIGH = 3
    """Must be a member of the server for longer than 10 minutes."""

    VERY_HIGH = 4
    """Must have a verified phone number."""


class OnboardingMode(IntEnum):
    ONBOARDING_DEFAULT = 0
    """Counts only Default Channels towards constraints."""

    ONBOARDING_ADVANCED = 1
    """Counts Default Channels and Questions towards constraints."""


class PromptType(IntEnum):
    MULTIPLE_CHOICE = 0
    DROPDOWN = 1
