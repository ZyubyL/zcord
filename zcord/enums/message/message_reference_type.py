from __future__ import annotations

from enum import IntEnum


class MessageReferenceType(IntEnum):
    """
    Type of referenced message.

    | Type | Value | Description |
    |------|-------|-------------|
    | `DEFAULT` | `0` | A message reply. |
    | `FORWARD` | `1` | A forwarded message. |
    """

    DEFAULT = 0
    FORWARD = 1
