from __future__ import annotations

from enum import IntEnum


class InteractionType(IntEnum):
    """
    | Name | Value |
    |------|-------|
    | `PING` | `1` |
    | `APPLICATION_COMMAND` | `2` |
    | `MESSAGE_COMPONENT` | `3` |
    | `APPLICATION_COMMAND_AUTOCOMPLETE` | `4` |
    | `MODAL_SUBMIT` | `5` |
    """

    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5


class InteractionContextType(IntEnum):
    """
    | Name | Value | Description |
    |------|-------|-------------|
    | `GUILD` | `0` | Interaction can be used within servers. |
    | `BOT_DM` | `1` | Interaction can be used within DMs with the app's bot. |
    | `PRIVATE_CHANNEL` | `2` | Interaction can be used within Group DMs and \
                                DMs other than the app's bot. |
    """

    GUILD = 0
    BOT_DM = 1
    PRIVATE_CHANNEL = 2


class InteractionCallbackType(IntEnum):
    """
    | Name | Value | Description |
    |------|-------|-------------|
    | `PONG` | `1` | ACK for a `PING` interaction. |
    | `CHANNEL_MESSAGE_WITH_SOURCE` | `4` | Respond to an interaction \
    with a message. |
    | `DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE` | `5` | ACK for an interaction \
    and edit the response later. |
    | `DEFERRED_UPDATE_MESSAGE` | `6` | ACK for an interaction and update \
    the original message later[^1]. |
    | `UPDATE_MESSAGE` | `7` | Edit the message the component was attached \
    to[^1]. |
    | `APPLICATION_COMMAND_AUTOCOMPLETE_RESULT` | `8` | Respond to an \
    autocomplete interaction with suggested choices. |
    | `MODAL` | `9` | Respond to an interaction with a modal.[^2] |
    | `LAUNCH_ACTIVITY` | `12` | Launch the activity associated with the \
    interaction. |

    [^1]: Only valid for [`Component`][zcord.Component] based interactions.
    [^2]: Not available for `MODAL_SUBMIT` and `PING` interactions.
    """

    PONG = 1
    CHANNEL_MESSAGE_WITH_SOURCE = 4
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5
    DEFERRED_UPDATE_MESSAGE = 6
    UPDATE_MESSAGE = 7
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8
    MODAL = 9
    LAUNCH_ACTIVITY = 12
