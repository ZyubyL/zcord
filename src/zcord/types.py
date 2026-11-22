from __future__ import annotations

from typing import Literal

__all__ = [
    "AnimatedFormat",
    "ImageFormat",
    "TupleOrList",
]

type TupleOrList[T] = list[T] | tuple[T, ...]
"""For type checking, if a parameter is of these types"""

type ImageFormat = Literal["png", "jpg", "jpeg", "webp"]
"""Non-animated image formats."""

type AnimatedFormat = Literal[ImageFormat, "gif"]
"""Image formats with animated ones"""
