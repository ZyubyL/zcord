import asyncio
import datetime

import config

import zcord
from zcord.enums import BaseThemeType


async def send_embed(bot):
    name = "ZyubyL"
    url = "https://github.com/thqnhz"
    img_url = "https://github.com/thqnhz.png"

    embed = (
        zcord.Embed.new()
        .set_url(url)
        .set_title("title")
        .set_description("description")
        .set_timestamp(datetime.datetime(2067, 6, 7))
        .set_footer(text=name, icon_url=img_url)
        .set_image(url=img_url)
        .set_thumbnail(url=img_url)
        .set_author(
            name=name,
            url=url,
            icon_url=img_url,
        )
        .add_field(name="field name", value="field value")
        .add_field(name="no inline", value="set inline to False", inline=False)
    )
    m = await bot._state.send_message(config.CHANNEL_ID, embeds=[embed])
    print(m)


async def send_poll(bot):
    poll = (
        zcord.Poll.new()
        .set_question("Do you like Zcord?")
        .set_answers(
            [
                "Heck yeah",
                "Booo",
            ]
        )
        .set_duration(1)
        .set_multiselect(True)
    )
    m = await bot._state.send_message(config.CHANNEL_ID, poll=poll)
    print(m)


async def send_shared_client_theme(bot):
    shared_client_theme = (
        zcord.SharedClientTheme.new()
        .set_colors(["1E1E2E"])
        .set_gradient_angle(67)
        .set_base_mix(69)
        .set_base_theme(BaseThemeType.MIDNIGHT)
    )
    m = await bot._state.send_message(
        config.CHANNEL_ID, shared_client_theme=shared_client_theme
    )
    print(m)


async def main():
    async with zcord.Bot(config.DISCORD_TOKEN) as bot:
        # await send_embed(bot)
        # await send_poll(bot)
        await send_shared_client_theme(bot)


asyncio.run(main())
