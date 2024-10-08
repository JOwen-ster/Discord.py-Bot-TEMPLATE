import asyncio
import bot
import discord
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
    # Do other async actions
    await confirmation()
    # Start the bot
    async with discordbot:
        await discordbot.start(TOKEN)

asyncio.run(main())

# IMPORTANT
# YOU MUST USE TYPE HINTS FOR ALL PARAMETERS WITH COG SLASH COMMANDS (application commands)
# OR ELSE SELF@class WILL BE PASSED AS THE INTERACTION
# https://github.com/Rapptz/discord.py/discussions/8372

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst

# https://github.com/Rapptz/discord.py/tree/master/examples