import asyncio
import bot
import discord
from os import getenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
discordbot = bot.Bot(command_prefix='^', intents=intents, help_command=None)

async def confirmation():
    print('Ran main')

async def main() -> None:
    # do other async actions
    await confirmation()

    # start the client
    async with discordbot:
        await discordbot.start(TOKEN)

asyncio.run(main())

# YOU MUST USE TYPE HINTS FOR ALL PARAMS WITH COG SLASH/APPLICATION COMMANDS OR SELF WILL BE PASSED AS THE INTERACTION
#https://github.com/Rapptz/discord.py/discussions/8372

#COG EXAMPLE
# https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be?permalink_comment_id=3488145
