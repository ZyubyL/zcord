import config

import zcord
from zcord import MISSING


async def main():
    """
    [[**READ THIS**]]

    You can rename `config.py.example` to `config.py` and fill in your bot \
    token and channel ID.

    You should not commit your bot token to version control.
    """
    async with zcord.Bot(config.DISCORD_TOKEN) as bot:
        application = await bot.fetch_current_application()
        assert application.bot is not MISSING
        channel = await bot.fetch_channel(config.CHANNEL_ID)
        await channel.send(
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
                .set_title(application.name)
                .set_description(application.description)
                .set_author(
                    name=f"{application.bot.username}#{application.bot.discriminator}",
                    url="https://github.com/thqnhz/zcord",
                    icon_url=application.icon_url or MISSING,
                )
            )
            .add_shared_client_theme(
                zcord.SharedClientTheme.new()
                .add_color("11111b")
                .add_colors(["181825", "1e1e2e"])
                .set_gradient_angle(67)
                .set_base_mix(69)
            )
        )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
