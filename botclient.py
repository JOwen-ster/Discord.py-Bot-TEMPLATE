from cogs import extensions
import asyncpg
from discord.ext import commands
from utils.loggingsetup import getlog
import db.custom_query


class Bot(commands.Bot):
    def __init__(self, *args, db_pool: asyncpg.Pool = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_pool: asyncpg.Pool | None = db_pool
        self.cog_counter = 0

    async def setup_hook(self) -> None:
        getlog().info('Running bot setup_hook...')
        for i, cog in enumerate(extensions, 1):
            try:
                await self.load_extension(f'cogs.{cog}')
                getlog().info(f'{cog} cog loaded ({i}/{len(extensions)})')
            except Exception as e:
                getlog().error(f'Could not load {cog} cog ({i}/{len(extensions)}): {e}')

        if self.db_pool:
            async with self.db_pool.acquire() as conn:
                version = await conn.fetchval('SELECT version();')
                name = await conn.fetchval('SELECT current_database();')
                db_msg = f'Connected to {name} database on {version}'
                getlog().info(db_msg)
                print(db_msg)
        else:
            invalid_db_msg = 'No Database Pool Found. Skiping...'
            getlog().info(invalid_db_msg)
            print(invalid_db_msg)

        getlog().info('Ran bot setup_hook!')

    async def on_ready(self) -> None:
        tree = await self.tree.sync() # pass in a guild object to test commands on that guild
        ready_msg_tree = f'Synced {len(tree)} tree commands.'
        ready_msg_cogs = f"Loaded {len(extensions)} {'cogs' if len(extensions) > 1 else 'cog'}"
        bot_ready_msg = 'Bot ready'

        getlog().info(ready_msg_cogs)
        getlog().info(ready_msg_tree)
        getlog().info(bot_ready_msg)
        print(ready_msg_cogs)
        print(ready_msg_tree)
        print(bot_ready_msg)

    async def query(self, sql_stmt: str, *args, mode: str = "fetch"):
        return await db.custom_query.custom_sql_query(
            db_pool=self.db_pool,
            sql_query=sql_stmt,
            *args,
            mode=mode
        )
