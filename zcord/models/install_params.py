from __future__ import annotations

from dataclasses import dataclass

from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class InstallParams(Model):
    """
    Settings for the app's default in-app authorization link.
    """

    scopes: tuple[str, ...]
    """
    The scopes[^1] to request during installation.

    [^1]: https://docs.discord.com/developers/topics/oauth2#shared-resources
    """

    permissions: str
    """
    The permissions to request for the bot role.
    """
