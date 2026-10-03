from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from zcord.types import AnimatedFormat, ImageFormat

__all__ = ["CDN"]

_BASE_URL = "https://cdn.discordapp.com"
_MIN_SIZE = 16
_MAX_SIZE = 4096
_FORMATS = frozenset({"png", "jpg", "jpeg", "webp", "gif"})


def _build(path: str, hash: str, size: int, format: str | None) -> str:
    if not _MIN_SIZE <= size <= _MAX_SIZE or size & (size - 1):
        raise ValueError(
            f"Size must be a power of 2 between {_MIN_SIZE} and {_MAX_SIZE},"
            f" got {size}"
        )
    if format is not None and format not in _FORMATS:
        raise ValueError(f"Unsupported format: {format!r}")
    format = format or ("gif" if hash.startswith("a_") else "png")
    return f"{_BASE_URL}/{path}/{hash}.{format}?size={size}"


class CDN:
    MIN_SIZE = _MIN_SIZE
    """
    The minimum size of a CDN image.
    """

    MAX_SIZE = _MAX_SIZE
    """
    The maximum size of a CDN image.
    """

    @staticmethod
    def application_icon(
        *,
        app_id: int,
        hash: str,
        size: int,
        format: ImageFormat | None,
    ) -> str:
        return _build(f"/app-icons/{app_id}", hash, size, format)

    @staticmethod
    def user_avatar(
        *,
        user_id: int,
        hash: str,
        size: int,
        format: AnimatedFormat | None,
    ) -> str:
        return _build(f"/avatars/{user_id}", hash, size, format)

    @staticmethod
    def user_banner(
        *,
        user_id: int,
        hash: str,
        size: int,
        format: str | None,
    ) -> str:
        return _build(f"/banners/{user_id}", hash, size, format)

    @staticmethod
    def avatar_decoration(
        *,
        hash: str,
        size: int,
    ) -> str:
        return _build("/avatar-decoration-presets", hash, size, "png")

    @staticmethod
    def emoji(
        *,
        hash: str,
        size: int,
        format: AnimatedFormat | None,
    ) -> str:
        return _build("/emojis", hash, size, format)

    @staticmethod
    def badge(
        *,
        guild_id: int,
        hash: str,
        size: int,
        format: ImageFormat | None,
    ) -> str:
        return _build(f"/guild-tag-badges/{guild_id}", hash, size, format)

    @staticmethod
    def guild_icon(
        *,
        guild_id: int,
        hash: str,
        size: int,
        format: AnimatedFormat | None,
    ) -> str:
        return _build(f"/icons/{guild_id}", hash, size, format)

    @staticmethod
    def guild_banner(
        *,
        guild_id: int,
        hash: str,
        size: int,
        format: AnimatedFormat | None,
    ) -> str:
        return _build(f"/banners/{guild_id}", hash, size, format)

    @staticmethod
    def team_icon(
        *,
        team_id: int,
        hash: str,
        size: int,
        format: ImageFormat | None,
    ) -> str:
        return _build(f"/team-icons/{team_id}", hash, size, format)
