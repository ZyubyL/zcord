# Zcord Documentation

Welcome to Zcord documentation page.

!!! note

    ***The project is still in development!***

## Installation

```bash
# pip
pip install zcord

# uv
uv add zcord
```

## Example

Detailed examples are available in the [examples directory](https://github.com/thqnhz/zcord/tree/master/examples) on GitHub.

```py
import zcord


async def main():
    """You should not commit your bot token to version control."""
    async with zcord.Bot(
        "your token here",
        intents=None  # You don't need websocket for this
    ):
        await (
            zcord.Message.new()
            .set_content("Hello, from Zcord!")
            .add_embed(
                zcord.Embed.new()
                .set_title("This is an embed")
                .set_description("Sent using Zcord embed builder")
            )
            .send(1234567)  # replace with your channel ID
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Usage

Zcord is split into submodules:

- [`zcord`](api/zcord.md) - Contains the core classes.
- [`zcord.errors`](api/errors.md) - Contains error from the library.
- [`zcord.bitfields`](api/bitfields.md) - Contains bitfield flag types.
- [`zcord.enums`](api/enums.md) - Contains enum types.

## Class Diagram

See the [class diagram](class_diagram.md).
