import asyncio
import datetime
import time

import config

import zcord


async def main():
    async with zcord.Bot(config.DISCORD_TOKEN) as bot:
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
            .add_field(
                name="no inline", value="set inline to False", inline=False
            )
        )
        m = await bot._state.send_message(config.CHANNEL_ID, embeds=[embed])
        print(m)


asyncio.run(main())
