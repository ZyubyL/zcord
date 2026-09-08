from __future__ import annotations

from dataclasses import dataclass

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model
from zcord.models.snowflake import Snowflake


@dataclass
class _MessageCreate(Model):
    """
    Private class for sending message.
    """

    sticker_ids: tuple[Snowflake, ...] | MISSING = MISSING
    flags: bitfields.MessageFlags | MISSING = MISSING

    @classmethod
    def new(
        cls,
        *,
        sticker_ids: tuple[int | Snowflake, ...]
        | list[int | Snowflake]
        | MISSING = MISSING,
        flags: bitfields.MessageFlags | MISSING = MISSING,
    ) -> _MessageCreate:
        if not sticker_ids or sticker_ids is MISSING:
            sticker_ids = MISSING
        elif len(sticker_ids) > 3:
            raise ValueError("Cannot send more than 3 stickers.")
        else:
            sticker_ids = tuple(Snowflake(sticker) for sticker in sticker_ids)
        if (
            flags is not MISSING
            and not flags & bitfields.MessageFlags._SEND_MESSAGE_FLAGS
        ):
            raise ValueError(
                f"""
                Only `SUPPRESS_EMBEDS`, `SUPPRESS_NOTIFICATIONS`, \
                `IS_VOICE_MESSAGE`, `IS_COMPONENTS_V2` can be set.
                Got {flags!r} instead.
                """
            )
        return _MessageCreate(sticker_ids=sticker_ids, flags=flags)
