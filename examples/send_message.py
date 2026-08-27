import contextlib

import config

import zcord
import zcord.enums as zenums
from zcord import MISSING

zcord.setup_logging()


async def main():
    """
    [[**READ THIS**]]

    You can rename `config.py.example` to `config.py` and fill in your bot \
    token and channel ID.

    You should not commit your bot token to version control.
    """
    async with zcord.Bot(config.DISCORD_TOKEN, intents=None) as bot:
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
                    .set_style(zenums.ButtonStyle.LINK)
                    .set_url("https://github.com/thqnhz/zcord")
                )
            )
        )
        await bot.start()


if __name__ == "__main__":
    import asyncio

    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
