from __future__ import annotations

from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from zcord.types import AnimatedFormat, ImageFormat

VALID_SIZES = frozenset[int]({16, 32, 64, 128, 256, 512, 1024, 2048, 4096})
"""The valid sizes of a CDN image."""

VALID_FORMATS = frozenset[str]({"png", "jpg", "jpeg", "webp", "gif", "json"})
"""The valid formats of a CDN image."""

BASE_URL = "https://cdn.discordapp.com"


def custom_emoji(
    *,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build("/emojis", hash, size, format)


def guild_icon(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/icons/{guild_id}", hash, size, format)


def guild_splash(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/splashes/{guild_id}", hash, size, format)


def guild_discovery_splash(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/discovery-splashes/{guild_id}", hash, size, format)


def guild_banner(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/banners/{guild_id}", hash, size, format)


def user_banner(
    *,
    user_id: int,
    hash: str,
    size: int,
    format: str | None,
) -> str:
    return _build(f"/banners/{user_id}", hash, size, format)


def default_user_avatar(
    *,
    index: str,
    size: int,
) -> str:
    return _build("/embed/avatars", index, size, "png")


def user_avatar(
    *,
    user_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/avatars/{user_id}", hash, size, format)


def guild_member_avatar(
    *,
    guild_id: int,
    user_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(
        f"/guilds/{guild_id}/users/{user_id}/avatars", hash, size, format
    )


def avatar_decoration(
    *,
    hash: str,
    size: int,
) -> str:
    return _build("/avatar-decoration-presets", hash, size, "png")


def application_icon_cover(
    *,
    app_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    """
    Including:
        - Application Icon
        - Application Cover
    """
    return _build(f"/app-icons/{app_id}", hash, size, format)


def application_asset(
    *,
    app_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/app-assets/{app_id}", hash, size, format)


def achievement_icon(
    *,
    app_id: int,
    achievement_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(
        f"/app-assets/{app_id}/achievements/{achievement_id}/icons",
        hash,
        size,
        format,
    )


# NOTE: What is wrong with Discord documentation
def store_page_asset(
    *,
    app_id: int,
    asset_id: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    # I would assume they meant to replace asset_id with actual asset_id
    return _build(f"/app-assets/{app_id}/store", asset_id, size, format)


# NOTE: This one too?
def sticker_pack_banner(
    *,
    # I would assume they didn't mean to hardcode an app id?
    # app_id: int,
    sticker_pack_banner_asset_id: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    # TODO: Change this if they actually did
    return _build(
        "/app-assets/710982414301790216/store",
        sticker_pack_banner_asset_id,
        size,
        format,
    )


def team_icon(
    *,
    team_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/team-icons/{team_id}", hash, size, format)


def sticker(
    *,
    sticker_id: int,
    size: int,
    format: ImageFormat | Literal["json"] | None,
) -> str:
    return _build("/stickers", str(sticker_id), size, format)


def role_icon(
    *,
    role_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/role-icons/{role_id}", hash, size, format)


def guild_scheduled_event_cover(
    *,
    scheduled_event_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/guild-events/{scheduled_event_id}", hash, size, format)


def guild_member_banner(
    *,
    guild_id: int,
    user_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(
        f"/guilds/{guild_id}/users/{user_id}/banners", hash, size, format
    )


def guild_tag_badge(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/guild-tag-badges/{guild_id}", hash, size, format)


def _build(path: str, hash: str, size: int, format: str | None) -> str:
    if size not in VALID_SIZES:
        raise ValueError(f"Size must be one of {VALID_SIZES}, got {size}")
    if format is not None and format not in VALID_FORMATS:
        raise ValueError(f"Unsupported format: {format!r}")
    format = format or ("gif" if hash.startswith("a_") else "png")
    return f"{BASE_URL}{path}/{hash}.{format}?size={size}"
