from __future__ import annotations

from datetime import UTC, datetime

import config

import zcord
from zcord import MISSING


async def main():
    async with zcord.Bot(config.DISCORD_TOKEN) as bot:
        app = await bot._state.fetch_current_application()
        assert app.bot is not MISSING
        assert app.owner is not MISSING
        embed = (
            zcord.Embed.new()
            .set_title(app.name)
            .set_description(app.description)
            .set_thumbnail(app.icon_url or MISSING)
            .set_timestamp(datetime.now(UTC))
            .set_author(
                name=f"{app.bot.username}#{app.bot.discriminator}",
                icon_url=app.bot.avatar_url or MISSING,
            )
            .set_footer(
                text=app.owner.username,
                icon_url=app.owner.avatar_url or MISSING,
            )
            .set_image(app.bot.banner_url or MISSING)
        )

        await bot._state.send_message(config.CHANNEL_ID, embeds=[embed])


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
