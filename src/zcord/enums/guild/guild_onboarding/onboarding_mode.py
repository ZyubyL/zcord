from enum import IntEnum


class OnboardingMode(IntEnum):
    ONBOARDING_DEFAULT = 0
    """Counts only Default Channels towards constraints."""

    ONBOARDING_ADVANCED = 1
    """Counts Default Channels and Questions towards constraints."""
