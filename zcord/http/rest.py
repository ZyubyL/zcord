from __future__ import annotations

from typing import TYPE_CHECKING

from zcord.errors import HTTPError, MutuallyExclusiveParamsError
from zcord.missing import MISSING
from zcord.models import (
    Channel,
    Guild,
    Message,
    Snowflake,
    Sticker,
    StickerPack,
    User,
)
from zcord.models.base import ZcordModel

if TYPE_CHECKING:
    from zcord.http import HTTPClient


def _build_query(**params) -> str:
    filtered = {}
    for k, v in params.items():
        if v is MISSING:
            continue
        if isinstance(v, bool):
            v = str(v).lower()
        filtered[k] = v
    if not filtered:
        return ""
    return "?" + "&".join(f"{k}={v}" for k, v in filtered.items())


def _mutually_exclusive(**params) -> None:
    passed = [name for name, value in params.items() if value is not MISSING]
    if len(passed) > 1:
        raise MutuallyExclusiveParamsError(
            f"Expected only 1 parameters from {', '.join(params)}"
            f", got {len(passed)}: {', '.join(passed)}"
        )


class REST:
    @staticmethod
    async def send_message(
        http: HTTPClient, channel_id: int | Snowflake | Channel, **kwargs
    ) -> Message:
        """
        Send a message to a channel.
        """
        serialized = {}
        for k, v in kwargs.items():
            if v is MISSING:
                continue
            if isinstance(v, list) and isinstance(v[0], ZcordModel):
                serialized[k] = [val._to_payload() for val in v]
            elif isinstance(v, ZcordModel):
                serialized[k] = v._to_payload()
            else:
                serialized[k] = v
        resp = await http.request(
            "POST",
            f"/channels/{int(channel_id)}/messages",
            json=serialized,
        )
        return Message._from_payload(dict(resp))

    @staticmethod
    async def fetch_channel_messages(
        http: HTTPClient,
        channel_id: int | Snowflake,
        *,
        around: int | Snowflake | MISSING = MISSING,
        before: int | Snowflake | MISSING = MISSING,
        after: int | Snowflake | MISSING = MISSING,
        limit: int = 50,
    ) -> list[Message]:
        """
        Fetch the messages in a channel.

        Params:
            channel_id:
                The channel to fetch the messages.
            around:
                Get messages around this message ID.
            before:
                Get messages before this message ID.
            after:
                Get messages after this message ID.

        Notes:
            `around`, `before` and `after` are mutually exclusive.

        Returns:
            A list of [`Message`][] from newest to oldest.

        Raises
            HTTPError:
                The request failed.
            MutuallyExclusiveParamsError:
                Parameters which mutually exclusive to each other have been \
                passed.
            ValueError:
                An incorrect value of `limit` has been passed.
        """
        _mutually_exclusive(around=around, before=before, after=after)
        if limit <= 0 or limit > 100:
            raise ValueError(f"Expected 1-100 messages, got {limit}")
        endpoint = f"/channels/{channel_id}/messages"
        endpoint += _build_query(
            around=around, before=before, after=after, limit=limit
        )
        resp = await http.request("GET", endpoint)
        return [Message._from_payload(m) for m in resp]

    @staticmethod
    async def fetch_channel_message(
        http: HTTPClient,
        *,
        channel_id: int | Snowflake,
        message_id: int | Snowflake,
    ) -> Message:
        """
        Fetch a specific message in a channel.

        Params:
            channel_id:
                The channnel ID to get the message.
            message_id:
                The message ID.

        Returns:
            A Discord [`Message`][].

        Raise:
            HTTPError:
                The request failed.
        """
        endpoint = f"/channels/{channel_id}/messages/{message_id}"
        resp = await http.request("GET", endpoint)
        return Message._from_payload(dict(resp))

    @staticmethod
    async def fetch_guild(
        http: HTTPClient,
        guild_id: int | Snowflake,
        *,
        with_counts: bool | MISSING = MISSING,
    ) -> Guild:
        """
        Fetch a guild with guild ID.

        Returns:
            A Discord [`Guild`][].

        Raises:
            HTTPError:
                The request failed.
        """
        endpoint = f"/guilds/{guild_id}{_build_query(with_counts=with_counts)}"
        resp = await http.request("GET", endpoint)
        return Guild._from_payload(dict(resp))

    @staticmethod
    async def fetch_sticker(
        http: HTTPClient, *, sticker_id: int | Snowflake
    ) -> Sticker:
        """
        Fetch a sticker with its ID.

        Returns:
            A Discord [`Sticker`][].

        Raises:
            HTTPError:
                The request failed.
        """
        resp = await http.request("GET", f"/stickers/{sticker_id}")
        return Sticker._from_payload(dict(resp))

    @staticmethod
    async def fetch_sticker_packs(http: HTTPClient) -> list[StickerPack]:
        """
        Fetch a list of available sticker packs.

        Returns:
            A list of Discord [`StickerPack`][].

        Raises:
            HTTPError:
                The request failed.
        """
        resp = await http.request("GET", "/sticker-packs")
        return [
            StickerPack._from_payload(r) for r in dict(resp)["sticker_packs"]
        ]

    @staticmethod
    async def fetch_sticker_pack(
        http: HTTPClient, *, pack_id: int | Snowflake
    ) -> StickerPack:
        """
        Fetch a sticker pack by ID.

        Returns:
            A Discord [`StickerPack`][].

        Raises:
            HTTPError:
                The request failed.
        """
        resp = await http.request("GET", f"/sticker-packs/{pack_id}")
        return StickerPack._from_payload(dict(resp))

    @staticmethod
    async def fetch_guild_stickers(
        http: HTTPClient, *, guild_id: int | Snowflake | Guild
    ) -> list[Sticker]:
        """
        Fetch all guild stickers.

        Returns:
            A list of [`Sticker`][]s.

        Raises:
            HTTPError:
                The request failed.
        """
        resp = await http.request("GET", f"/guilds/{int(guild_id)}/stickers")
        return [Sticker._from_payload(r) for r in resp]

    @staticmethod
    async def fetch_guild_sticker(
        http: HTTPClient,
        *,
        guild_id: int | Snowflake | Guild,
        sticker_id: int | Snowflake,
    ) -> Sticker:
        """
        Fetch a specific guild sticker.

        Returns:
            A [`Sticker`].

        Raises:
            HTTPError:
                The request failed.
        """
        resp = await http.request(
            "GET", f"/guilds/{int(guild_id)}/stickers/{sticker_id}"
        )
        return Sticker._from_payload(dict(resp))

    @staticmethod
    async def create_guild_sticker(
        http: HTTPClient,
        *,
        guild_id: int | Snowflake | Guild,
        name: str,
        description: str = "",
        tags: str = "",
        file,
    ) -> Sticker:
        """|Not implemented|
        Create a new sticker for the guild.

        Params:
            name:
                The sticker name (2-30 character long).
            description:
                The sticker description (either empty or 2-100 character long).
            tags:
                The sticker tags for autocomplete/suggestion \
                (max 200 characters).
            file:
                The sticker to upload.

        Returns:
            The newly uploaded sticker.

        Raises:
            HTTPError:
                The request failed.
        """
        raise NotImplementedError

    @staticmethod
    async def edit_guild_sticker(
        http: HTTPClient,
        *,
        guild_id: int | Snowflake | Guild,
        sticker_id: int | Snowflake,
        name: str,
        description: str | None = None,
        tags: str,
    ) -> Sticker:
        """|Not implemented|
        Modify the given sticker.

        Params:
            name:
                The updated name of the sticker (2-30 character long).
            description:
                The updated description of the sticker \
                (`None` to keep the old one, 2-100 character long if update).
            tags:
                The updated tags of the sticker (max 200 characters).
        """
        raise NotImplementedError

    @staticmethod
    async def delete_guild_sticker(
        http: HTTPClient,
        *,
        guild_id: int | Snowflake | Guild,
        sticker_id: int | Snowflake | Sticker,
    ) -> bool:
        """
        Delete the given sticker.

        Returns:
            If the request is successful or not.

        Raises:
            HTTPError:
                The request failed.
        """
        # TODO: Maybe create a method in client.py to only get the return code
        async with http.session as cs:
            resp = await cs.request(
                "DELETE", f"/guilds/{guild_id}/stickers/{sticker_id}"
            )
            if resp.status == 204:
                return True
            raise HTTPError(f"{resp.status} {resp.reason}")

    @staticmethod
    async def fetch_answer_voters(
        http: HTTPClient,
        *,
        channel_id: int | Snowflake | Channel,
        message_id: int | Snowflake | Message,
        answer_id: int,
        after: int | Snowflake | MISSING = MISSING,
        limit: int = 50,
    ) -> list[User]:
        """
        Fetch the voters for a given answer in a poll.

        Returns:
            A list of users who voted for the answer.

        Raises:
            HTTPError:
                The request failed.
            ValueError:
                Wrong limit amount has been provided.
        """
        if limit < 1 or limit > 100:
            raise ValueError("limit must be between 1 and 100")
        endpoint = (
            f"/channels/{int(channel_id)}/polls/{int(message_id)}/answers/{answer_id}"
            + _build_query(after=after, limit=limit)
        )
        resp = await http.request("GET", endpoint)
        return [User._from_payload(user) for user in dict(resp)["users"]]

    @staticmethod
    async def end_poll(
        http: HTTPClient,
        *,
        channel_id: int | Snowflake | Channel,
        message_id: int | Snowflake | Message,
    ) -> Message:
        """
        End a poll and return the updated message.

        Returns:
            The updated message after the poll has been ended.

        Raises:
            HTTPError:
                The request failed.
        """
        endpoint = f"/channels/{int(channel_id)}/polls/{int(message_id)}/expire"
        resp = await http.request("POST", endpoint)
        return Message._from_payload(dict(resp))
