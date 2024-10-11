import cogs
from discord.ext import commands
from utils.loggingsetup import getlog


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        getlog().info('Running bot setup_hook...')
        for i, cog in enumerate(cogs.names, 1):
            try:
                await self.load_extension('cogs.' + cog)
                getlog().info(F'Loaded {cog} cog ({i}/{len(cogs.names)})')
            except:
                getlog().info(F'Could not load cog.{cog} ({i}/{len(cogs.names)})')
        getlog().info('Ran bot setup_hook')

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        getlog().info(F'Synced {len(tree)} tree commands. Bot ready')
        print(F'Synced {len(tree)} tree commands. Bot ready')