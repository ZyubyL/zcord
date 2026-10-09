from __future__ import annotations

import sys

if sys.version_info >= (3, 15):
    from builtins import sentinel
else:
    from typing_extensions import sentinel

MISSING = sentinel("MISSING")
"""
A special marker indicating that a value was not provided.

Notes:
    Unlike [`None`][], `MISSING` means the parameter **was omitted entirely**.
"""
