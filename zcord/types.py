from __future__ import annotations

__all__ = [
    "TupleOrList",
]

type TupleOrList[T] = list[T] | tuple[T, ...]
"""For type checking, if a parameter is of these types"""
