"""Zcord - Minimalistic Discord API Wrapper."""

from ._logging import setup_logging
from ._version import __version__
from .missing import MISSING

__all__ = [
    "MISSING",
    "__version__",
    "setup_logging",
]
