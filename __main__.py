import asyncio
import discord.ext.commands
import bot
import discord
import logging
import logging.handlers
from dotenv import load_dotenv
from os import getenv

import discord.ext

load_dotenv()
if not (TOKEN := getenv("DISCORD_BOT_TOKEN")):
    print('Token environment variable is empty.')
    exit(1)

intents = discord.Intents.default()
intents.message_content = True
discordbot = bot.Bot(command_prefix='^', intents=intents, help_command=None)

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord_bot.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)

dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

async def confirmation():
    logger.info('Created Discord Bot Instance.')

async def main() -> None:
    # Run other async tasks
    # USE ASYNC TASK GROUPS TO DO MULTIPLE TASKS AT A SINGLE TIME FOR EASY PARALLEL PROCESSING
    # https://docs.python.org/3/library/asyncio-task.html#task-groups
    await confirmation()
    # Start the bot
    try:
        async with discordbot:
            await discordbot.start(TOKEN)
    except:
        print('Invalid Token')
        exit(1)

asyncio.run(main())

# Examples
# https://github.com/Rapptz/discord.py/tree/master/docs
# https://github.com/Rapptz/discord.py/tree/master/examples

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst