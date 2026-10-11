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

    PING = 1  # TODO: HTTP-only interaction handling

    APPLICATION_COMMAND = 2
    """
    The [`Interaction`][zcord.Interaction] came from an application command.
    """

    MESSAGE_COMPONENT = 3
    """
    The [`Interaction`][zcord.Interaction] came from a \
    [`Component`][zcord.Component].
    """

    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    """
    The [`Interaction`][zcord.Interaction] came from a \
    slash command autocompletion.
    """

    MODAL_SUBMIT = 5
    """
    The [`Interaction`][zcord.Interaction] came from a [`Modal`][] submission.
    """
