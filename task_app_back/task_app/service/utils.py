import os
import asyncpg
import psycopg2
import psycopg2.extras


NAME = os.environ["PGSQL_USER"]
PASS = os.environ["PGSQL_PASS"]
HOST = os.environ["PGSQL_HOST"]
PORT = os.environ["PGSQL_PORT"]
DB_NAME = os.environ["PGSQL_DB"]
DEFAULT_DATABASE_CURSOR_OPTION = {"cursor_factory": psycopg2.extras.DictCursor}


async def _async_get_connection() -> asyncpg.connection.Connection:
    url = f"postgresql://{NAME}:{PASS}@{HOST}:{PORT}/{DB_NAME}"
    return await asyncpg.connect(url)
    

class AsyncDatabaseConnector:
    def __init__(self, option = None):
        self.option = self.option = DEFAULT_DATABASE_CURSOR_OPTION if option is None else option
        self.conn = None
    
    async def __aenter__(self) -> asyncpg.connection.Connection:
        self.conn = await _async_get_connection()
        return self.conn
    
    async def __aexit__(self, ex_type, ex_value, trace) -> None:
        await self.conn.close()