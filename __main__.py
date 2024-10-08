import asyncio
import bot
import discord
import logging
import logging.handlers
from dotenv import load_dotenv
from os import getenv


load_dotenv()
if not (TOKEN := getenv("DISCORD_BOT_TOKEN")):
    print('Token environment variable is empty.')
    exit(1)

intents = discord.Intents.default()
discordbot = bot.Bot(command_prefix='^', intents=intents, help_command=None)

async def confirmation():
    print('Created Discord Bot Instance.')

async def main() -> None:
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    await confirmation()
    # Start the bot
    async with discordbot:
        await discordbot.start(TOKEN)

asyncio.run(main())


# Examples
# https://github.com/Rapptz/discord.py/tree/master/docs
# # https://github.com/Rapptz/discord.py/tree/master/examples

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst