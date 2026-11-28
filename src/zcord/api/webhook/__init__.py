"""Read more at https://docs.discord.com/developers/resources/webhook"""

from .enums import WebhookType
from .models import Webhook

__all__ = [
    "Webhook",
    "WebhookType",
]
