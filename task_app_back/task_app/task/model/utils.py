import os
import psycopg2
import psycopg2.extras

NAME = os.environ["PGSQL_USER"]
PASS = os.environ["PGSQL_PASS"]
HOST = os.environ["PGSQL_HOST"]
PORT = os.environ["PGSQL_PORT"]
DB_NAME = os.environ["PGSQL_NAME"]

def _get_connection():
    url = f"postgresql://{NAME}:{PASS}@{HOST}:{PORT}/{DB_NAME}"
    return psycopg2.connect(url)


def query_execute(
    query: str,
    values: tuple[str] = None,
    fetch: str = None,
    retrue_dict: bool = True
):
    assert  fetch in (None, "fetchall", "fetchone")

    opt = {}
    if retrue_dict:
        opt = {"cursor_factory": psycopg2.extras.DictCursor}


    with _get_connection() as conn:
        with conn.cursor(**opt) as cur:
            cur.execute(query=query, vars=values)

            if fetch is not None:
                res = getattr(cur, fetch)()

        conn.commit()
    
    if fetch is not None:
        return res