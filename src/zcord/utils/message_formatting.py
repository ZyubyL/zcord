"""Discord message formatting."""

from __future__ import annotations

from typing import TYPE_CHECKING

from zcord.enums import GuildNavigationTypes
from zcord.missing import MISSING

if TYPE_CHECKING:
    from zcord.enums import TimestampStyles
    from zcord.snowflake import Snowflake


def user_mention(id: Snowflake | int | str) -> str:
    """Convert this user ID to a Discord user mention."""
    return f"<@{id}>"


def channel_mention(id: Snowflake | int | str) -> str:
    """Convert this channel ID to a Discord channel mention."""
    return f"<#{id}>"


def role_mention(id: Snowflake | int | str) -> str:
    """Convert this role ID to a Discord role mention."""
    return f"<@&{id}>"


def game_profile_mention(id: Snowflake | int | str) -> str:
    """Convert this game ID to a Discord game mention."""
    return f"<@${id}>"


def slash_command_mention(name: str, id: Snowflake | int | str) -> str:
    """Convert this slash command name and ID \
    to a Discord slash command mention."""
    return f"</{name}:{id}>"


def group_slash_command_mention(
    group: str, name: str, id: Snowflake | int | str
) -> str:
    """Convert this slash command with its group name and ID \
    to a Discord slash command mention."""
    return f"</{group} {name}:{id}>"


def group_subgroup_slash_command_mention(
    group: str, subgroup: str, name: str, id: Snowflake | int | str
) -> str:
    """Convert this slash command with its outer group, sub group, name and ID \
    to a Discord slash command mention."""
    return f"</{group} {subgroup} {name}:{id}>"


def custom_emoji(name: str, id: Snowflake | int | str) -> str:
    """Convert the name and ID to a custom emoji."""
    return f"<:{name}:{id}>"


def animated_custom_emoji(name: str, id: Snowflake | int | str) -> str:
    """Convert the name and ID to a custom animated emoji."""
    return f"<a:{name}:{id}>"


def unix_timestamp(
    timestamp: int, format: TimestampStyles | str | MISSING = MISSING
) -> str:
    """Convert this Unix timestamp to Discord message format."""
    format = f":{format}" if format is not MISSING else ""
    return f"<t:{timestamp}{format}>"


def guild_navigation(type: GuildNavigationTypes | str) -> str:
    """Convert this guild nagivation type to its Discord message format."""
    return f"<id:{type}>"


# TODO: Role object too?
def linked_role(id: Snowflake | int | str) -> str:
    """Convert this linked role ID to Discord message format."""
    return f"<id:{GuildNavigationTypes.LINKED_ROLES}:{id}>"
