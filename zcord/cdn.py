_BASE_URL = "https://cdn.discordapp.com"


def _check_animated(hash: str) -> bool:
    return hash.startswith("a_")


def _pick_best_format(format: str | None, hash: str) -> str:
    if format is None:
        return "gif" if _check_animated(hash) else "png"
    return format


class CDN:
    MAX_SIZE = 4096

    @staticmethod
    def application_icon(
        *,
        app_id: int,
        hash: str,
        size: int,
        format: str | None,
    ) -> str:
        format = _pick_best_format(format, hash)
        return f"{_BASE_URL}/app-icons/{app_id}/{hash}.{format}?size={size}"

    @staticmethod
    def user_avatar(
        *,
        user_id: int,
        hash: str,
        size: int,
        format: str | None,
    ) -> str:
        format = _pick_best_format(format, hash)
        return f"{_BASE_URL}/avatars/{user_id}/{hash}.{format}?size={size}"

    @staticmethod
    def user_banner(
        *,
        user_id: int,
        hash: str,
        size: int,
        format: str | None,
    ) -> str:
        format = _pick_best_format(format, hash)
        return f"{_BASE_URL}/banners/{user_id}/{hash}.{format}?size={size}"

    @staticmethod
    def avatar_decoration(
        *,
        hash: str,
        size: int,
    ) -> str:
        return f"{_BASE_URL}/avatar-decoration-presets/{hash}.png?size={size}"
