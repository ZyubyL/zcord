from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord.enums.shared_client_theme import BaseThemeType
from zcord.missing import MISSING
from zcord.models.base import ZcordModel


@dataclass(frozen=True, slots=True)
class SharedClientTheme(ZcordModel):
    """
    Represent a shared client theme.

    Attributes:
        colors:
            A list of colors of the theme.
        gradient_angle:
            The direction of the theme's colors (max 360).
        base_mix:
            The intensity of the theme's colors (max 100).
        base_theme:
            The mode of the theme.
    """

    colors: tuple[str, ...] | MISSING = MISSING
    gradient_angle: int | MISSING = MISSING
    base_mix: int | MISSING = MISSING
    base_theme: BaseThemeType = BaseThemeType.UNSET

    _transforms: ClassVar[dict] = {
        "base_theme": BaseThemeType,
    }

    def _to_payload(self) -> dict:
        if self.colors is MISSING:
            raise ValueError("colors must be provided")
        if (
            self.gradient_angle is MISSING
            or self.gradient_angle < 0
            or self.gradient_angle > 360
        ):
            raise ValueError("gradient_angle must be between 0 and 360")
        if self.base_mix is MISSING or self.base_mix < 0 or self.base_mix > 100:
            raise ValueError("base_mix must be between 0 and 100")
        payload = ZcordModel._to_payload(self)
        return payload

    @classmethod
    def new(
        cls,
        *,
        colors: tuple[str, ...] | list[str] | MISSING = MISSING,
        gradient_angle: int | MISSING = MISSING,
        base_mix: int | MISSING = MISSING,
        base_theme: BaseThemeType = BaseThemeType.UNSET,
    ) -> SharedClientTheme:
        """*|classmethod|*

        Create a new shared client theme.
        """
        return (
            cls()
            .set_colors(colors if colors is not MISSING else ())
            .set_base_mix(base_mix if base_mix is not MISSING else 0)
            .set_base_theme(base_theme)
            .set_gradient_angle(gradient_angle)
        )

    def add_color(self, color: str) -> SharedClientTheme:
        """
        Add a color to the theme.
        """
        if self.colors is not MISSING and len(self.colors) >= 5:
            raise ValueError("Cannot add more than 5 colors to the theme.")
        return replace(
            self,
            colors=(*self.colors, color)
            if self.colors is not MISSING
            else (color,),
        )

    def add_colors(
        self, colors: tuple[str, ...] | list[str]
    ) -> SharedClientTheme:
        """
        Add multiple colors to the theme.
        """
        theme = self
        for color in colors:
            theme = theme.add_color(color)
        return theme

    def set_colors(
        self, colors: tuple[str, ...] | list[str]
    ) -> SharedClientTheme:
        """
        Set the colors of the theme.

        Warning:
            This will **remove** all the old colors.
            If you want to add color to the theme, use `add_color(s)` instead.
        """
        theme = self.clear_colors()
        for color in colors:
            theme = theme.add_color(color)
        return theme

    def clear_colors(self) -> SharedClientTheme:
        """
        Clear all the colors of the theme.
        """
        return replace(self, colors=MISSING)

    def set_gradient_angle(
        self, angle: int | MISSING = MISSING
    ) -> SharedClientTheme:
        """
        Set the gradient angle of the theme.
        """
        return replace(self, gradient_angle=angle)

    def set_base_mix(
        self, base_mix: int | MISSING = MISSING
    ) -> SharedClientTheme:
        """
        Set the base mix of the theme.
        """
        return replace(self, base_mix=base_mix)

    def set_base_theme(
        self, base_theme: BaseThemeType = BaseThemeType.UNSET
    ) -> SharedClientTheme:
        """
        Set the base theme of the theme.
        """
        return replace(self, base_theme=base_theme)
