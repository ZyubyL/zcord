"""
Send a message to a channel when the bot starts up.
"""

import asyncio

import config

import zcord
from zcord import MISSING, enums

zcord.setup_logging()

bot = zcord.Bot(
    # Change the config.py.example to config.py and add your bot token
    config.DISCORD_TOKEN,
    # Putting intents to None means the bot will not open websocket connections
    intents=None,
)


async def main():
    async with bot:
        application = await bot.fetch_current_application()
        bot_user = await bot.fetch_current_user()
        channel = await bot.fetch_channel(config.CHANNEL_ID)
        await channel.send(
            zcord.Message.new()
            .set_content("Hello, from Zcord!")
            .set_poll(
                zcord.Poll.new()
                .set_question("Do you like Zcord?")
                .add_answer(
                    text="Yes", emoji=zcord.Emoji.new("\N{THUMBS UP SIGN}")
                )
                .add_answer(text="Maybe", emoji="\N{SHRUG}")
                .add_answer(text="No", emoji="<a:crossout:1358833476979261702>")
                .set_duration(67)
            )
            .add_embed(
                zcord.Embed.new()
                .set_title(application.name)
                .set_description(application.description)
                .set_author(
                    name=f"{bot_user.username}#{bot_user.discriminator}",
                    url="https://github.com/thqnhz/zcord",
                    icon_url=application.icon_url() or MISSING,
                )
                .set_footer(
                    text=f"Zcord version {zcord.__version__}",
                    icon_url=bot_user.avatar_url() or MISSING,
                )
                .set_image(bot_user.banner_url() or MISSING)
            )
            .set_shared_client_theme(
                zcord.SharedClientTheme.new()
                .add_color("11111b")
                .add_colors(["181825", "1e1e2e"])
                .set_gradient_angle(67)
                .set_base_mix(69)
            )
            .add_component(
                zcord.ActionRow.new().add_button(
                    zcord.Button.new()
                    .set_label("View source")
                    .set_style(enums.ButtonStyle.LINK)
                    .set_url("https://github.com/thqnhz/zcord")
                )
            )
        )


asyncio.run(main())
