from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

from zcord.cdn import CDN
from zcord.flags import ApplicationFlags
from zcord.missing import MISSING
from zcord.models.base import ZcordModel
from zcord.models.guild import Guild
from zcord.models.snowflake import Snowflake
from zcord.models.user import User


@dataclass(frozen=True, slots=True)
class Application(ZcordModel):
    """
    Represent a Discord Application.

    Attributes:
        id:
            The ID of the app.
        name:
            The name of the app.
        icon:
            Icon hash of the app.
        description:
            The description of the app.
        rpc_origin:
            A list of RPC origin URLs, if RPC is enabled.
        bot_public:
            Whether the bot is a public bot.
        bot_require_code_grant:
            Whether a full OAuth2 code grant flow is needed to add the bot.
        bot:
            The bot user of the app.
        term_of_service_url:
            The app's ToS URL.
        privacy_policy_url:
            The app's Privacy Policy URL.
        owner:
            The owner of the bot.
        verify_key:
            Hex encoded key for verification in interaction.
        team:
            A list of member from the app's team, if the app belongs to one.
        guild_id:
            The guild ID associated with the app.
        guild:
            The guild associated with the app.
        primary_sku_id:
            If the app is a game sold on Discord, this field is the ID of the \
            Game SKU that is created.
        slug:
            If the app is a game sold on Discord, this field is the URL slug \
            that links to the store page.
        cover_image:
            The cover image hash for the app's default rich presence invite.
        flags:
            The app's public flags.
        approximate_guild_count:
            The appoximated number of guilds the app has been added to.
        approximate_user_install_count:
            The approximated number of users that have installed the app.
        approximate_user_authorization_count:
            The approximated number of users that have OAuth2 authorization \
            for the app.
        redirect_uris:
            A list of redirect URIs for the app.
        interactions_endpoint_url:
            The interactions endpoint URL for the app.
        role_connections_verification_url:
            Role connection verification URL for the app.
        event_webhooks_url:
            Webhook URL for the app to receive webhook events.
        event_webhooks_status:
            Status of the app's webhook events.
        event_webhooks_types:
            A list of webhook event types the app subscribes to.
        tags:
            A list of tags describing the content and functionality of the app.
        install_params:
            Settings for the app's default in-app authorization link.
        integration_types_config:
            Default scopes and permissions for each supported installation \
            context.
        custom_install_url:
            Default custom authorization URL for the app.
    """

    id: Snowflake
    name: str
    icon: str | None
    description: str
    bot_public: bool
    bot_require_code_grant: bool
    verify_key: str
    team: Any | None
    rpc_origin: list[str] | MISSING = MISSING
    bot: User | MISSING = MISSING
    term_of_service_url: str | MISSING = MISSING
    privacy_policy_url: str | MISSING = MISSING
    owner: User | MISSING = MISSING
    guild_id: Snowflake | MISSING = MISSING
    guild: Guild | MISSING = MISSING
    primary_sku_id: Snowflake | MISSING = MISSING
    slug: str | MISSING = MISSING
    cover_image: str | MISSING = MISSING
    flags: ApplicationFlags | MISSING = MISSING
    approximate_guild_count: int | MISSING = MISSING
    approximate_user_install_count: int | MISSING = MISSING
    approximate_user_authorization_count: int | MISSING = MISSING
    redirect_uris: list[str] | MISSING = MISSING
    interactions_endpoint_url: str | None | MISSING = MISSING
    role_connections_verification_url: str | None | MISSING = MISSING
    event_webhooks_url: str | None | MISSING = MISSING
    event_webhooks_status: Any | MISSING = MISSING
    event_webhooks_types: list[str] | MISSING = MISSING
    tags: list[str] | MISSING = MISSING
    install_params: Any | MISSING = MISSING
    integration_types_config: dict | MISSING = MISSING
    custom_install_url: str | MISSING = MISSING

    _transforms: ClassVar[dict] = {
        "id": Snowflake,
        "bot": User,
        "flags": ApplicationFlags,
        "owner": User,
        "guild_id": Snowflake,
        "guild": Guild,
        "primary_sku_id": Snowflake,
    }

    @property
    def icon_url(self) -> str | None:
        """The application icon URL if available."""
        if not self.icon:
            return None
        return CDN.application_icon(self.id, self.icon)
