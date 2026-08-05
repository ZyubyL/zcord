import config

import zcord


async def main():
    """
    [[**READ THIS**]]

    You can rename `config.py.example` to `config.py` and fill in your bot \
    token and channel ID.

    You should not commit your bot token to version control.
    """
    async with zcord.Bot(config.DISCORD_TOKEN):
        await (
            zcord.Message.new()
            .set_content("Hello, from Zcord!")
            .set_poll(
                zcord.Poll.new()
                .set_question("Do you like Zcord?")
                .set_answers(["Yes", "No :("])
                .add_answer("Maybe :shrug:")
                .set_duration(67)
            )
            .add_embed(
                zcord.Embed.new()
                .set_title("This is an embed")
                .set_description("Sent using Zcord embed builder")
            )
            .send(config.CHANNEL_ID)
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
