import cogs
from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        print('Running bot setup_hook...')
        for i, cog in enumerate(cogs.names, 1):
            try:
                await self.load_extension('cogs.' + cog)
                print(F'Loaded cog.{cog} ({i}/{len(cogs.names)})')
            except:
                print(F'Could not load cog.{cog} ({i}/{len(cogs.names)})')
        print('Ran setup_hook')

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        print(F'Synced {len(tree)} tree commands')