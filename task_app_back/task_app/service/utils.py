import os
import psycopg2
import psycopg2.extras
from psycopg2.extensions import connection, cursor


NAME = os.environ["PGSQL_USER"]
PASS = os.environ["PGSQL_PASS"]
HOST = os.environ["PGSQL_HOST"]
PORT = os.environ["PGSQL_PORT"]
DB_NAME = os.environ["PGSQL_DB"]
DEFAULT_DATABASE_CURSOR_OPTION = {"cursor_factory": psycopg2.extras.DictCursor}


def _get_connection() -> connection:
    url = f"postgresql://{NAME}:{PASS}@{HOST}:{PORT}/{DB_NAME}"
    return psycopg2.connect(url)


class DatabaseConnector:
    def __init__(self, option = None):
        self.option = DEFAULT_DATABASE_CURSOR_OPTION if option is None else option
        self.conn = None
        self.cur = None

    def __enter__(self) -> cursor:
        self.conn = _get_connection()
        self.cur = self.conn.cursor(**self.option)
        return self.cur

    def __exit__(self, ex_type, ex_value, trace) -> None:
        self.cur.close()
        self.conn.commit()
        self.conn.close()

