"""Read more at https://docs.discord.com/developers/resources/entitlement"""

from .enums import EntitlementType
from .models import Entitlement

__all__ = [
    "Entitlement",
    "EntitlementType",
]
