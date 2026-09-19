# Zcord Documentation

Welcome to Zcord documentation page.

!!! note

    ***The project is still in development!***

## TL;DR
<div class="grid cards" markdown>

-   :simple-python:{ .lg .middle } __Python 3.12+__

    [:octicons-arrow-right-24: Go to install](#installation)

-   :fontawesome-solid-exclamation-circle:{ .lg .middle } __Gateway and HTTP-only (WIP)__

    [:octicons-arrow-right-24: See examples](#example)

-   :material-api:{ .lg .middle } __Usage__

    [:octicons-arrow-right-24: See API references](api/zcord)

-   :material-update:{ .lg .middle } __News and update__

    [:octicons-arrow-right-24: See Changelog](CHANGELOG)

</div>

## Installation

=== "Using pip"
    ```sh
    pip install zcord
    ```
=== "Using uv"
    ```sh
    uv add zcord
    ```

## Example

Detailed examples are available in the [examples directory](https://github.com/zyubyl/zcord/tree/master/examples) on GitHub.

!!! note
    You should not commit your bot token to version control.

=== "HTTP-only bot example"

    ``` py title="http_bot.py"
    import zcord
    
    bot = zcord.Bot(
        "your token here",
        intents=None,  # You don't need a websocket for this
    )
    
    
    async def main():
        async with bot:
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

=== "Gateway bot example"

    ``` py title="gateway_bot.py"
    import zcord
    from zcord import bitfields
    from zcord.enums import GatewayEvent
    
    bot = zcord.Bot(
        "your token here",
        intents=(
            # To receive message events from the guild from the gateway
            bitfields.Intents.GUILD_MESSAGES
            # To receive message content from the gateway
            | bitfields.Intents.MESSAGE_CONTENT
            # ^ Use the OR operator `|` to combine the bitfields
        ),
    )
    
    
    # Bot.once will only fire once on the first time the event is fired
    @bot.once(GatewayEvent.READY)
    def once_ready(user: zcord.User):
        print(user.username)
    
    
    async def on_message(message: zcord.Message):
        if message.content is not MISSING and message.content.lower() == "hello":
            await message.reply(zcord.Message.new(content="hi"))
    
    
    # You can also pass callback function to the method
    bot.on(GatewayEvent.MESSAGE_CREATE, on_message)
    
    # Start the bot
    bot.run()
    ```

## Usage

Zcord is split into submodules:

- [`zcord`](api/zcord.md) - Contains the core classes.
- [`zcord.errors`](api/errors.md) - Contains error from the library.
- [`zcord.bitfields`](api/bitfields.md) - Contains bitfield flag types.
- [`zcord.enums`](api/enums.md) - Contains enum types.

## Changelog

See the [changelog](CHANGELOG.md).

## Class Diagram

See the [class diagram](class_diagram.md).
