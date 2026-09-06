"""
Reply with "hello" when the bot receives a message with "hi".

(Demonstrates the gateway event)

This example requires `MESSAGE_CONTENT` intent.
"""

import logging

import config

import zcord
from zcord import MISSING, bitfields, enums

log = logging.getLogger(__name__)

zcord.setup_logging(logging.DEBUG)

bot = zcord.Bot(
    # Change the config.py.example to config.py and add your bot token
    config.DISCORD_TOKEN,
    intents=(
        bitfields.Intents.GUILD_MESSAGES | bitfields.Intents.MESSAGE_CONTENT
    ),
)


@bot.on(enums.GatewayEvent.MESSAGE_CREATE)
async def on_message_create(message: zcord.Message) -> None:
    if message.content is not MISSING and message.content.lower() == "hi":
        await message.reply(zcord.Message.new(content="hello"))


# Alternatively, you can pass the callback directly
# The callback is also not required to be asynchronous
# @bot.once(enums.GatewayEvent.READY)  # Instead of this
def on_ready(user: zcord.User) -> None:
    log.info("%s is ready", user.username)


bot.once(enums.GatewayEvent.READY, on_ready)  # You do this


bot.run()
