from __future__ import annotations

import sys

if sys.version_info >= (3, 15):
    from builtins import sentinel
else:
    from typing_extensions import sentinel

MISSING = sentinel("MISSING")
"""A marker for a value that was not provided.

Notes:
    This is different from [`None`][], `None` means the value is explicitly \
    set to "no value."
"""
