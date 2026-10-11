from __future__ import annotations

from enum import IntEnum


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
