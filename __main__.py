import asyncio
import botclient
import discord
from utils.loggingsetup import getlog
from dotenv import load_dotenv
from os import getenv


intents = discord.Intents.default()
intents.message_content = True
discordbot = botclient.Bot(command_prefix='}', intents=intents, help_command=None)

load_dotenv()
if not (TOKEN := getenv("DISCORD_BOT_TOKEN")):
    getlog().error('Token is empty.')
    exit(1)

async def confirmation():
    getlog().info('Created Discord Bot Instance.')

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
        getlog().error('Invalid Token')
        exit(1)

asyncio.run(main())

# Examples
# https://github.com/Rapptz/discord.py/tree/master/docs
# https://github.com/Rapptz/discord.py/tree/master/examples

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst