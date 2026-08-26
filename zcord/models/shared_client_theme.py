from __future__ import annotations

from dataclasses import dataclass, replace
from typing import ClassVar

from zcord import enums
from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class SharedClientTheme(Model):
    """
    Represent a shared client theme.
    """

    colors: tuple[str, ...] | MISSING = MISSING
    """
    A list of colors of the theme.
    """

    gradient_angle: int | MISSING = MISSING
    """
    The direction of the theme's colors (max 360).
    """

    base_mix: int | MISSING = MISSING
    """
    The intensity of the theme's colors (max 100).
    """

    base_theme: enums.BaseThemeType = enums.BaseThemeType.UNSET
    """
    The mode of the theme.
    """

    _transforms: ClassVar[dict] = {
        "base_theme": enums.BaseThemeType,
    }

    def _check_before(self) -> None:
        if self.colors is MISSING:
            raise ValueError("colors must be provided")
        if self.gradient_angle is MISSING:
            raise ValueError("gradient_angle must be provided")
        if self.base_mix is MISSING:
            raise ValueError("base_mix must be provided")

    @classmethod
    def new(
        cls,
        *,
        colors: tuple[str, ...] | list[str] | MISSING = MISSING,
        gradient_angle: int | MISSING = MISSING,
        base_mix: int | MISSING = MISSING,
        base_theme: enums.BaseThemeType = enums.BaseThemeType.UNSET,
    ) -> SharedClientTheme:
        """
        Create a new shared client theme.
        """
        return (
            cls()
            .set_colors(colors)
            .set_base_mix(base_mix)
            .set_base_theme(base_theme)
            .set_gradient_angle(gradient_angle)
        )

    def add_color(self, color: str) -> SharedClientTheme:
        """
        Add a color to the theme.

        Raises:
            ValueError:
                - Cannot add more than 5 colors to the theme.
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

        Raises:
            ValueError:
                - Cannot add more than 5 colors to the theme.
        """
        theme = self
        for color in colors:
            theme = theme.add_color(color)
        return theme

    def set_colors(
        self, colors: tuple[str, ...] | list[str] | MISSING = MISSING
    ) -> SharedClientTheme:
        """
        Set the colors of the theme.

        Raises:
            ValueError:
                - Cannot add more than 5 colors to the theme.

        Warning:
            This will **remove** all the old colors.
            If you want to add color to the theme, use `add_color(s)` instead.
        """
        theme = self.clear_colors()
        if colors is not MISSING:
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

        Raises:
            ValueError:
                gradient_angle must be between 0 and 360.
        """
        if angle is not MISSING and (angle < 0 or angle > 360):
            raise ValueError("gradient_angle must be between 0 and 360")
        return replace(self, gradient_angle=angle)

    def set_base_mix(
        self, base_mix: int | MISSING = MISSING
    ) -> SharedClientTheme:
        """
        Set the base mix of the theme.

        Raises:
            ValueError:
                base_mix must be between 0 and 100.
        """
        if base_mix is not MISSING and (base_mix < 0 or base_mix > 100):
            raise ValueError("base_mix must be between 0 and 100")
        return replace(self, base_mix=base_mix)

    def set_base_theme(
        self, base_theme: enums.BaseThemeType = enums.BaseThemeType.UNSET
    ) -> SharedClientTheme:
        """
        Set the base theme of the theme.
        """
        return replace(self, base_theme=base_theme)
