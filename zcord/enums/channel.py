from __future__ import annotations

from enum import IntEnum


class ChannelType(IntEnum):
    """Represent the type of a Discord channel.

    | Name | Value | Description |
    |------|-------|-------------|
    | `GUILD_TEXT` | `0` | A text channel in a guild. |
    | `DM` | `1` |   A direct message channel. |
    | `GUILD_VOICE` | `2` | A voice channel in a guild. |
    | `GROUP_DM` | `3` | A group direct message channel. |
    | `GUILD_CATEGORY` | `4` | A guild category. |
    | `GUILD_ANNOUNCEMENT` | `5` | A guild news channel. |
    | `ANNOUNCEMENT_THREAD` | `10` | A thread in a `GUILD_ANNOUNCEMENT` \
                                     channel. |
    | `PUBLIC_THREAD` | `11` | A thread in a `GUILD_TEXT` \
                               or `GUILD_FORUM` channel. |
    | `PRIVATE_THREAD` | `12` | A private thread in a `GUILD_TEXT` \
                                or `GUILD_FORUM` channel. |
    | `GUILD_STAGE_VOICE` | `13` | A stage channel in a guild. |
    | `GUILD_DIRECTORY` | `14` | The channel in a hub containing \
                                 the listed servers. |
    | `GUILD_FORUM` | `15` | A thread-only channel. |

    Notes:
        `GUILD_MEDIA (16)` is unstable so this library won't add it.
    """

    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_ANNOUNCEMENT = 5
    ANNOUNCEMENT_THREAD = 10
    PUBLIC_THREAD = 11
    PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13
    GUILD_DIRECTORY = 14
    GUILD_FORUM = 15
    # GUILD_MEDIA = 16  # unstable
