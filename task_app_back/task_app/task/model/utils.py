import psycopg2
from .struct import Task

NAME = "postgres"
PASS = "password"
HOST = "localhost"


def _get_connection():
    url = f"postgresql://{NAME}:{PASS}@{HOST}"
    return psycopg2.connect(url)


def query_execute(
    query: str,
    values: tuple[str] = None,
    fetch: str = None
):
    assert  fetch in (None, "fetchall", "fetchone")

    with _get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query=query, vars=values)

            if fetch is not None:
                res = getattr(cur, fetch)()

        conn.commit()
    
    if fetch is not None:
        return res