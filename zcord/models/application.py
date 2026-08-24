from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar, Literal

from zcord import bitfields
from zcord.cdn import CDN
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.guild import Guild
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Application(Model):
    """
    Represent a Discord Application.
    """

    id: Snowflake
    """
    The ID of the app.
    """

    name: str
    """
    The name of the app.
    """

    icon: str | None
    """
    Icon hash of the app.
    """

    description: str
    """
    The description of the app.
    """

    bot_public: bool
    """
    Whether the bot is a public bot.
    """

    bot_require_code_grant: bool
    """
    Whether a full OAuth2 code grant flow is needed to add the bot.
    """

    verify_key: str
    """
    Hex encoded key for verification in interaction.
    """

    team: Any | None
    """
    A list of member from the app's team, if the app belongs to one.
    """

    rpc_origin: tuple[str, ...] | MISSING = MISSING
    """
    A list of RPC origin URLs, if RPC is enabled.
    """

    bot: User | MISSING = MISSING
    """
    The bot user of the app.
    """

    term_of_service_url: str | MISSING = MISSING
    """
    The app's ToS URL.
    """

    privacy_policy_url: str | MISSING = MISSING
    """
    The app's Privacy Policy URL.
    """

    owner: User | MISSING = MISSING
    """
    The owner of the bot.
    """

    guild_id: Snowflake | MISSING = MISSING
    """
    The guild ID associated with the app.
    """

    guild: Guild | MISSING = MISSING
    """
    The guild associated with the app.
    """

    primary_sku_id: Snowflake | MISSING = MISSING
    """
    If the app is a game sold on Discord,
    this field is the ID of the Game SKU that is created.
    """

    slug: str | MISSING = MISSING
    """
    If the app is a game sold on Discord,
    this field is the URL slug that links to the store page.
    """

    cover_image: str | MISSING = MISSING
    """
    The cover image hash for the app's default rich presence invite.
    """

    flags: bitfields.ApplicationFlags | MISSING = MISSING
    """
    The app's public flags.
    """

    approximate_guild_count: int | MISSING = MISSING
    """
    The appoximated number of guilds the app has been added to.
    """

    approximate_user_install_count: int | MISSING = MISSING
    """
    The approximated number of users that have installed the app.
    """

    approximate_user_authorization_count: int | MISSING = MISSING
    """
    The approximated number of users that have OAuth2 authorization
    for the app.
    """

    redirect_uris: tuple[str, ...] | MISSING = MISSING
    """
    A list of redirect URIs for the app.
    """

    interactions_endpoint_url: str | None | MISSING = MISSING
    """
    The interactions endpoint URL for the app.
    """

    role_connections_verification_url: str | None | MISSING = MISSING
    """
    Role connection verification URL for the app.
    """

    event_webhooks_url: str | None | MISSING = MISSING
    """
    Webhook URL for the app to receive webhook events.
    """

    event_webhooks_status: Any | MISSING = MISSING
    """
    Status of the app's webhook events.
    """

    event_webhooks_types: tuple[str, ...] | MISSING = MISSING
    """
    A list of webhook event types the app subscribes to.
    """

    tags: tuple[str, ...] | MISSING = MISSING
    """
    A list of tags describing the content and functionality of the app.
    """

    install_params: Any | MISSING = MISSING
    """
    Settings for the app's default in-app authorization link.
    """

    integration_types_config: dict | MISSING = MISSING
    """
    Default scopes and permissions for each supported installation context.
    """

    custom_install_url: str | MISSING = MISSING
    """
    Default custom authorization URL for the app.
    """

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "bot": User,
        "flags": bitfields.ApplicationFlags,
        "owner": User,
        "guild_id": Snowflake,
        "guild": Guild,
        "primary_sku_id": Snowflake,
    }

    def icon_url(
        self,
        *,
        size: int = CDN.MAX_SIZE,
        format: Literal["png", "jpg", "jpeg", "webp"] | None = None,
    ) -> str | None:
        """
        The application icon URL if available.

        Notes:
            `size` needs to be a power of 2 between `16` and `4096`.
        """
        if not self.icon:
            return None
        return CDN.application_icon(
            app_id=self.id,
            hash=self.icon,
            size=size,
            format=format,
        )
