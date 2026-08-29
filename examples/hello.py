"""
Reply with "hello" when the bot receives a message with "hi".

(Demonstrates the gateway event)

This example requires `MESSAGE_CONTENT` intent.
"""

import logging

import config

import zcord
from zcord import MISSING, bitfields, enums

log = logging.getLogger(__file__)

bot = zcord.Bot(
    # Change the config.py.example to config.py and add your bot token
    config.DISCORD_TOKEN,
    intents=(
        bitfields.Intents.GUILD_MESSAGES | bitfields.Intents.MESSAGE_CONTENT
    ),
)


async def on_message_create(message: zcord.Message):
    if message.content is not MISSING and message.content.lower() == "hi":
        await message.reply(zcord.Message.new(content="hello"))


# Bot.once() will only run once when the event is fired
# Technically, you can use lambda for this if you don't care about typing
bot.once(enums.GatewayEvent.READY, lambda *_: log.info("Bot is ready"))
# Bot.on() will run every time the event is fired
bot.on(enums.GatewayEvent.MESSAGE_CREATE, on_message_create)

bot.run()
