from __future__ import annotations

from dataclasses import dataclass

from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedFooter(Model):
    """
    Contain embed's footer info.
    """

    text: str | MISSING = MISSING
    """
    Footer text.
    """

    icon_url: str | MISSING = MISSING
    """
    URL of footer icon.
    """

    proxy_icon_url: str | MISSING = MISSING
    """
    A proxied URL of footer icon.
    """

    @classmethod
    def new(
        cls, *, text: str | MISSING = MISSING, icon_url: str | MISSING = MISSING
    ) -> EmbedFooter:
        """
        Create a new embed footer.
        """
        return cls(text=text, icon_url=icon_url)
