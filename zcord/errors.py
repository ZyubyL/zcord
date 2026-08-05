from __future__ import annotations


class ZcordError(Exception):
    """Base exception for errors from Zcord."""


class MutuallyExclusiveParamsError(ZcordError):
    """Parameters which mutually exclusive with each other have been passed."""


class HTTPError(ZcordError):
    """The request returned non-OK code."""
