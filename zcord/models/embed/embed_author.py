from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedAuthor(Model):
    """
    Contain embed's author info.
    """

    name: str
    """
    The name of the author.
    """

    url: str | MISSING = MISSING
    """
    The URL of the author.
    """

    icon_url: str | MISSING = MISSING
    """
    The URL of the author icon.
    """

    proxy_icon_url: str | MISSING = MISSING
    """
    A proxied url of the author icon.
    """

    @classmethod
    def new(
        cls,
        name: str,
        url: str | MISSING = MISSING,
        icon_url: str | MISSING = MISSING,
    ) -> EmbedAuthor:
        """
        Create a new embed author.
        """
        return cls(name=name, url=url, icon_url=icon_url)
