import asyncio
import botclient
import discord
import asyncpg
import db.connection
from utils.loggingsetup import getlog
from dotenv import load_dotenv
from os import getenv


load_dotenv()
TOKEN = getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    getlog().error('Token is empty.')
    exit(1)

async def confirmation():
    getlog().info('Created Discord Bot Instance.')

async def main() -> None:
    # Run other async tasks
    await confirmation()

    # Setup Discord Bot Client
    intents: discord.Intents = discord.Intents.default()
    intents.message_content = True
    discord_bot = botclient.Bot(command_prefix='}', intents=intents, help_command=None)

    # Setup Postgre Database
    db_creds = list(db.connection.get_db_credentials().values())

    if all(db_creds):
        # Data Source Name
        POSTGRE_DSN = f'postgres://{db_creds['DB_USER']}:{db_creds['DB_PASS']}@{db_creds['DB_HOST']}:{db_creds['DB_PORT']}/{db_creds['DB_NAME']}'

        # Establish Database Pool Connection
        async with asyncpg.create_pool(dsn=POSTGRE_DSN) as pool:
            discord_bot.db_pool = pool

            # Start Discord Bot
            try:
                async with discord_bot:
                    await discord_bot.start(TOKEN)
                    conn = await discord_bot.db_pool.acquire()
                    version = conn.fetchval('SELECT version();')
                    version_msg = f'Connected to {db_creds['DB_NAME']} on Postgre Version: {version}'
                    getlog().info(version_msg)
                    print(version_msg)
            except Exception as error:
                print(error)
                getlog().error(error)
            finally:
                if discord_bot.db_pool:
                    await discord_bot.db_pool.close()
    else:
        try:
            async with discord_bot:
                await discord_bot.start(TOKEN)
        except Exception as error:
            getlog().error(error)
            print(error)

asyncio.run(main())

# Examples
# https://github.com/Rapptz/discord.py/tree/master/docs
# https://github.com/Rapptz/discord.py/tree/master/examples

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst