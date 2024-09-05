import asyncio
import bot
import cogs
import discord


intents = discord.Intents.default()
discordbot = bot.Bot(command_prefix='^', intents=intents, help_command=None)

@discordbot.event
async def on_ready() -> None:
    tree = await discordbot.tree.sync()
    print(F'Synced {len(tree)} tree commands')

async def confirm() -> None:
    print('Main Ran.')

async def main() -> None:
    # do other async actions
    await confirm()

    # start the client
    async with discordbot:
        for i, cog in enumerate(cogs.names, 1):
            try:
                await discordbot.load_extension('cogs.' + cog)
                print(F'Loaded cog.{cog} ({i}/{len(cogs.names)})')
            except:
                print(F'Could not load cog.{cog} ({i}/{len(cogs.names)})')
        await discordbot.start('MTE1NTc1ODA0NDQ2NzE3MTMyOA.Gn6OPh.vMGsnSg7qvG0YH46dEamHx7yG6kaoFDESefEfw')

asyncio.run(main())


#https://www.youtube.com/watch?v=_KZOe8-uhZI

# YOU MUST USE TYPE HINTS
#https://github.com/Rapptz/discord.py/discussions/8372