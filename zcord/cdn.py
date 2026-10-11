from __future__ import annotations

from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from zcord.types import AnimatedFormat, ImageFormat

__all__ = [
    "MAX_SIZE",
    "MIN_SIZE",
    "application_icon",
    "avatar_decoration",
    "badge",
    "emoji",
    "guild_banner",
    "guild_icon",
    "team_icon",
    "user_avatar",
    "user_banner",
]

MIN_SIZE: Final = 16
"""The minimum size of a CDN image."""

MAX_SIZE: Final = 4096
"""The maximum size of a CDN image."""

_BASE_URL = "https://cdn.discordapp.com"
_FORMATS = frozenset({"png", "jpg", "jpeg", "webp", "gif"})


def _build(path: str, hash: str, size: int, format: str | None) -> str:
    if not MIN_SIZE <= size <= MAX_SIZE or size & (size - 1):
        raise ValueError(
            f"Size must be a power of 2 between {MIN_SIZE} and {MAX_SIZE},"
            f" got {size}"
        )
    if format is not None and format not in _FORMATS:
        raise ValueError(f"Unsupported format: {format!r}")
    format = format or ("gif" if hash.startswith("a_") else "png")
    return f"{_BASE_URL}{path}/{hash}.{format}?size={size}"


def application_icon(
    *,
    app_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/app-icons/{app_id}", hash, size, format)


def user_avatar(
    *,
    user_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/avatars/{user_id}", hash, size, format)


def user_banner(
    *,
    user_id: int,
    hash: str,
    size: int,
    format: str | None,
) -> str:
    return _build(f"/banners/{user_id}", hash, size, format)


def avatar_decoration(
    *,
    hash: str,
    size: int,
) -> str:
    return _build("/avatar-decoration-presets", hash, size, "png")


def emoji(
    *,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build("/emojis", hash, size, format)


def badge(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/guild-tag-badges/{guild_id}", hash, size, format)


def guild_icon(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/icons/{guild_id}", hash, size, format)


def guild_banner(
    *,
    guild_id: int,
    hash: str,
    size: int,
    format: AnimatedFormat | None,
) -> str:
    return _build(f"/banners/{guild_id}", hash, size, format)


def team_icon(
    *,
    team_id: int,
    hash: str,
    size: int,
    format: ImageFormat | None,
) -> str:
    return _build(f"/team-icons/{team_id}", hash, size, format)
