from cogs import names
from discord.ext import commands
from utils.loggingsetup import getlog


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.cog_counter = 0

    async def setup_hook(self) -> None:
        getlog().info('Running bot setup_hook...')
        for i, cog in enumerate(names, 1):
            try:
                # Load all added cogs into the bot
                await self.load_extension('cogs.' + cog)
                getlog().info(F'Loaded {cog} cog ({i}/{len(names)})')
            except:
                getlog().info(F'Could not load cogs.{cog} ({i}/{len(names)})')
        getlog().info('Ran bot setup_hook')

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        getlog().info(F'Synced {len(tree)} tree commands. Bot ready')
        print(F'Synced {len(tree)} tree commands. Bot ready')
