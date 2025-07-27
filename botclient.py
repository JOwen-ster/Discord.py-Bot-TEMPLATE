from cogs import extensions
import asyncpg
from discord.ext import commands
from utils.loggingsetup import getlog


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_pool: asyncpg.Pool | None = None
        self.cog_counter = 0

    async def setup_hook(self) -> None:
        getlog().info('Running bot setup_hook...')
        for i, cog in enumerate(extensions, 1):
            try:
                # Load all added cogs into the bot
                await self.load_extension(f'cogs.{cog}')
                getlog().info(F'{cog} cog loaded ({i}/{len(extensions)})')
            except:
                getlog().info(F'Could not load {cog} cog ({i}/{len(extensions)})')
        getlog().info('Ran bot setup_hook!')

    async def on_ready(self) -> None:
        tree = await self.tree.sync()
        ready_msg_tree = f'Synced {len(tree)} tree commands.'
        ready_msg_cogs = f'Loaded {len(extensions)} {'cogs' if len(extensions) > 1 else 'cog'}'
        bot_ready_msg = 'Bot ready'

        getlog().info(ready_msg_cogs)
        getlog().info(ready_msg_tree)
        getlog().info(bot_ready_msg)
        print(ready_msg_cogs)
        print(ready_msg_tree)
        print(bot_ready_msg)

    async def query(self, sql_query: str):
        if self.db_pool:
            async with self.db_pool.acquire() as conn:
                await conn.fetch(sql_query)
                getlog().info(f'SENT_QUERY:\n{sql_query}')
