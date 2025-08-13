from utils.loggingsetup import getlog
from asyncpg import Pool


async def custom_sql_query(db_pool: Pool, sql_query: str, *args, mode: str):
    """
    Run a database query.

    :param db_pool: Database Connection Pool
    :param sql_query: SQL query string (can use $1, $2 placeholders for parameters)
    :param args: Parameters for the query
    :param mode: "fetch" (select many rows), "fetchval" (select single value), or "execute" (no row select)
    :return: Query result or None
    """
    if not db_pool:
        getlog().info('Cannot execute query, no database pool found.')
        return
    async with db_pool.acquire() as conn:
        match mode.lower():
            case 'fetch':
                result = await conn.fetch(sql_query, *args)
            case 'fetchval':
                result = await conn.fetchval(sql_query, *args)
            case 'execute':
                result = await conn.execute(sql_query, *args)
            case _:
                raise ValueError("Invalid mode. Use 'fetch', 'fetchval', or 'execute'.")
        getlog().info(f"QUERY_SENT - {sql_query} - values={args}")
        return result
