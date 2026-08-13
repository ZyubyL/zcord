_BASE_URL = "https://cdn.discordapp.com"


def _check_animated(hash: str) -> bool:
    return hash.startswith("a_")


class CDN:
    @staticmethod
    def application_icon(app_id: int, hash: str) -> str:
        return f"{_BASE_URL}/app-icons/{app_id}/{hash}.png"

    @staticmethod
    def user_avatar(user_id: int, hash: str) -> str:
        if _check_animated(hash):
            return f"{_BASE_URL}/avatars/{user_id}/{hash}.gif"
        return f"{_BASE_URL}/avatars/{user_id}/{hash}.png"

    @staticmethod
    def user_banner(user_id: int, hash: str) -> str:
        if _check_animated(hash):
            return f"{_BASE_URL}/banners/{user_id}/{hash}.gif"
        return f"{_BASE_URL}/banners/{user_id}/{hash}.png"

    @staticmethod
    def avatar_decoration(hash: str) -> str:
        return f"{_BASE_URL}/avatar-decoration-presets/{hash}.png"
