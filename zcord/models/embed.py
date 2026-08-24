from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime
from typing import ClassVar

from zcord import bitfields
from zcord.missing import MISSING
from zcord.models.base import Model


@dataclass(frozen=True, slots=True)
class EmbedFooter(Model):
    """
    Contain embed's footer info.
    """

    text: str | MISSING = MISSING
    """
    Footer text.
    """

    icon_url: str | MISSING = MISSING
    """
    URL of footer icon.
    """

    proxy_icon_url: str | MISSING = MISSING
    """
    A proxied URL of footer icon.
    """

    @classmethod
    def new(
        cls, *, text: str | MISSING = MISSING, icon_url: str | MISSING = MISSING
    ) -> EmbedFooter:
        """
        Create a new embed footer.
        """
        return cls(text=text, icon_url=icon_url)


@dataclass(frozen=True, slots=True)
class EmbedImage(Model):
    """
    Contain embed's image info.
    """

    url: str
    """
    Source URL of the image.
    """

    proxy_url: str | MISSING = MISSING
    """
    A proxied URL of the image.
    """

    height: int | MISSING = MISSING
    """
    The image's height.
    """

    width: int | MISSING = MISSING
    """
    The image's width.
    """

    content_type: str | MISSING = MISSING
    """
    The image's media type.
    """

    placeholder: str | MISSING = MISSING
    """
    Thumbhash placeholder of the image.
    """

    placeholder_version: int | MISSING = MISSING
    """
    Version of the placeholder.
    """

    description: str | MISSING = MISSING
    """
    Alt text of the image.
    """

    flags: bitfields.EmbedMediaFlags | MISSING = MISSING
    """
    Embed media flags combined as a bitfield.
    """

    _transforms: ClassVar[dict] = {
        "flags": bitfields.EmbedMediaFlags,
    }


@dataclass(frozen=True, slots=True)
class EmbedVideo(Model):
    """
    Contain embed's video info.
    """

    url: str | MISSING = MISSING
    """
    Source URL of the video.
    """

    proxy_url: str | MISSING = MISSING
    """
    A proxied URL of the video.
    """

    height: int | MISSING = MISSING
    """
    The video's height.
    """

    width: int | MISSING = MISSING
    """
    The video's width.
    """

    content_type: str | MISSING = MISSING
    """
    The video's media type.
    """

    placeholder: str | MISSING = MISSING
    """
    Thumbhash placeholder of the video.
    """

    placeholder_version: int | MISSING = MISSING
    """
    Version of the placeholder.
    """

    description: str | MISSING = MISSING
    """
    Alt text of the video.
    """

    flags: bitfields.EmbedMediaFlags | MISSING = MISSING
    """
    Embed media flags combined as a bitfield.
    """

    _transforms: ClassVar[dict] = {
        "flags": bitfields.EmbedMediaFlags,
    }


@dataclass(frozen=True, slots=True)
class EmbedProvider(Model):
    """
    Contain embed's provider info.
    """

    name: str | MISSING = MISSING
    """
    Name of the provider.
    """

    url: str | MISSING = MISSING
    """
    URL of the provider.
    """


@dataclass(frozen=True, slots=True)
class EmbedAuthor(Model):
    """
    Contain embed's author info.
    """

    name: str | MISSING = MISSING
    """
    The name of the author.
    """

    url: str | MISSING = MISSING
    """
    The URL of the author.
    """

    icon_url: str | MISSING = MISSING
    """
    The URL of the author icon.
    """

    proxy_icon_url: str | MISSING = MISSING
    """
    A proxied url of the author icon.
    """

    @classmethod
    def new(
        cls,
        name: str | MISSING = MISSING,
        url: str | MISSING = MISSING,
        icon_url: str | MISSING = MISSING,
    ) -> EmbedAuthor:
        """
        Create a new embed author.
        """
        return cls(name=name, url=url, icon_url=icon_url)


@dataclass(frozen=True, slots=True)
class EmbedField(Model):
    """
    Contain embed's field info.
    """

    name: str
    """
    The name of the field.
    """

    value: str
    """
    The value of the field.
    """

    inline: bool | MISSING = MISSING
    """
    Whether or not this field should display inline.
    """


@dataclass(frozen=True, slots=True)
class Embed(Model):
    """
    Represent a Discord embed.
    """

    title: str | MISSING = MISSING
    """
    Title of the embed.
    """

    type: str | MISSING = MISSING
    """
    Type of the embed.
    """

    description: str | MISSING = MISSING
    """
    Description of the embed.
    """

    url: str | MISSING = MISSING
    """
    URL of the embed.
    """

    timestamp: datetime | MISSING = MISSING
    """
    Timestamp of the embed.
    """

    color: int | MISSING = MISSING
    """
    Color of the embed.
    """

    footer: EmbedFooter | MISSING = MISSING
    """
    Embed's footer info.
    """

    image: EmbedImage | MISSING = MISSING
    """
    Embed's image info.
    """

    thumbnail: EmbedImage | MISSING = MISSING
    """
    Embed's thumbnail info.
    """

    video: EmbedVideo | MISSING = MISSING
    """
    Embed's video info.
    """

    provider: EmbedProvider | MISSING = MISSING
    """
    Embed's provider info.
    """

    author: EmbedAuthor | MISSING = MISSING
    """
    Embed's author info.
    """

    fields: tuple[EmbedField, ...] | MISSING = MISSING
    """
    Embed's field info.
    """

    flags: bitfields.EmbedFlags | MISSING = MISSING
    """
    Embed's flags combined as a bitfield.
    """

    _transforms: ClassVar[dict] = {
        "timestamp": datetime.fromisoformat,
        "footer": EmbedFooter,
        "image": EmbedImage,
        "thumbnail": EmbedImage,
        "video": EmbedVideo,
        "provider": EmbedProvider,
        "author": EmbedAuthor,
        "fields": EmbedField,
        "flags": bitfields.EmbedFlags,
    }

    def _check_before(self) -> None:
        if len(self) > 6000:
            raise ValueError("Embed must be 6000 characters or less.")

    def __len__(self) -> int:
        """
        Returns:
            The total character count of the embed.
        """
        count = 0
        if self.title is not MISSING:
            count += len(self.title)
        if self.description is not MISSING:
            count += len(self.description)
        if self.fields is not MISSING:
            for field in self.fields:
                count += len(field.name) + len(field.value)
        if self.footer is not MISSING and self.footer.text is not MISSING:
            count += len(self.footer.text)
        if self.image is not MISSING:
            count += len(self.image.url)
        if self.thumbnail is not MISSING:
            count += len(self.thumbnail.url)
        if self.author is not MISSING and self.author.name is not MISSING:
            count += len(self.author.name)
        return count

    @classmethod
    def new(
        cls,
        *,
        title: str | MISSING = MISSING,
        description: str | MISSING = MISSING,
        url: str | MISSING = MISSING,
        color: int | MISSING = MISSING,
        timestamp: datetime | MISSING = MISSING,
        footer: EmbedFooter | MISSING = MISSING,
        image_url: str | MISSING = MISSING,
        thumbnail_url: str | MISSING = MISSING,
        author: EmbedAuthor | MISSING = MISSING,
        fields: tuple[EmbedField, ...] | MISSING = MISSING,
    ) -> Embed:
        """
        Create a new embed.

        Examples:
            There are two ways to create an embed.

            1. Using the parameters in the `.new()` method.
            ```py
            embed = Embed.new(title="Foo", description="bar")
            ```

            2. Chaining the `.set_*()` methods.
            ```py
            embed = (
                Embed.new()
                .set_title("Foo")
                .set_description("bar")
            )
            ```

        Notes:
            Although you can technically use the class constructor, it is \
            recommended to use `.new()` instead.
        """
        embed = (
            cls(
                timestamp=timestamp,
                fields=fields,
                type="rich",
            )
            .set_url(url)
            .set_title(title)
            .set_description(description)
            .set_color(color)
            .set_image(image_url)
            .set_thumbnail(thumbnail_url)
        )
        if footer is not MISSING:
            embed = embed.set_footer(text=footer.text, icon_url=footer.icon_url)
        if author is not MISSING:
            embed = embed.set_author(
                name=author.name,
                url=author.url,
                icon_url=author.icon_url,
            )
        return embed

    def set_title(self, title: str | MISSING = MISSING) -> Embed:
        """
        Set the title of the embed.

        Raises:
            ValueError:
                Title must be 256 characters or less.
        """
        if title is not MISSING and len(title) > 256:
            raise ValueError("Title must be 256 characters or less.")
        return replace(self, title=title)

    def set_description(self, description: str | MISSING = MISSING) -> Embed:
        """
        Set the description of the embed.

        Raises:
            ValueError:
                Description must be 4096 characters or less.
        """
        if description is not MISSING and len(description) > 4096:
            raise ValueError("Description must be 4096 characters or less.")
        return replace(self, description=description)

    def set_url(self, url: str | MISSING = MISSING) -> Embed:
        """
        Set the URL of the embed.
        """
        return replace(self, url=url)

    def set_color(self, color: int | MISSING = MISSING) -> Embed:
        """
        Set the color of the embed.

        Raises:
            ValueError:
                Color must be an integer between 0x000000 and 0xFFFFFF.
        """
        if color is not MISSING and (color < 0 or color > 0xFFFFFF):
            raise ValueError(
                "Color must be an integer between 0x000000 and 0xFFFFFF."
            )
        return replace(self, color=color)

    def set_timestamp(self, timestamp: datetime | MISSING = MISSING) -> Embed:
        """
        Set the timestamp of the embed.
        """
        return replace(self, timestamp=timestamp)

    def set_footer(
        self,
        *,
        text: str | MISSING = MISSING,
        icon_url: str | MISSING = MISSING,
    ) -> Embed:
        """
        Set the footer of the embed.

        Raises:
            ValueError:
                Footer text cannot exceed 2048 characters.
        """
        if text is MISSING:
            return replace(self, footer=MISSING)
        if len(text) > 2048:
            raise ValueError("Footer text cannot exceed 2048 characters.")
        return replace(self, footer=EmbedFooter(text=text, icon_url=icon_url))

    def set_image(self, url: str | MISSING = MISSING) -> Embed:
        """
        Set the image of the embed.
        """
        if url is MISSING:
            return replace(self, image=MISSING)
        return replace(self, image=EmbedImage(url=url))

    def set_thumbnail(self, url: str | MISSING = MISSING) -> Embed:
        """
        Set the thumbnail of the embed.
        """
        if url is MISSING:
            return replace(self, thumbnail=MISSING)
        return replace(self, thumbnail=EmbedImage(url=url))

    def set_author(
        self,
        *,
        name: str | MISSING = MISSING,
        url: str | MISSING = MISSING,
        icon_url: str | MISSING = MISSING,
    ) -> Embed:
        """
        Set the author of the embed.

        Raises:
            ValueError:
                Author name cannot exceed 256 characters.

        Notes:
            Setting `name` to `MISSING` will remove the author.
        """
        if name is MISSING or not name:
            return replace(self, author=MISSING)
        if len(name) > 256:
            raise ValueError("Author name cannot exceed 256 characters.")
        return replace(
            self, author=EmbedAuthor(name=name, url=url, icon_url=icon_url)
        )

    def add_field(self, *, name: str, value: str, inline: bool = True) -> Embed:
        """
        Add a field to the embed.

        Params:
            name:
                The field name.
            value:
                The field value.
            inline:
                Whether the field should be inline.

        Raises:
            ValueError:
                - Field name cannot exceed 256 characters.
                - Field value cannot exceed 1024 characters.
                - Cannot add more than 25 fields to an embed.

        """
        if self.fields is not MISSING and len(self.fields) >= 25:
            raise ValueError("Cannot add more than 25 fields to an embed.")
        if len(name) > 256:
            raise ValueError("Field name cannot exceed 256 characters.")
        if len(value) > 1024:
            raise ValueError("Field value cannot exceed 1024 characters.")
        field = EmbedField(name=name, value=value, inline=inline)
        return replace(
            self,
            fields=(
                *self.fields,
                field,
            )
            if self.fields is not MISSING
            else (field,),
        )

    def remove_fields(self) -> Embed:
        """
        Remove all fields from the embed.
        """
        return replace(self, fields=MISSING)
