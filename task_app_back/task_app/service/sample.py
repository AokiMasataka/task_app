import datetime
import dataclasses
from uuid import UUID, uuid4


@dataclasses.dataclass
class Doc:
    id: UUID
    project_id: UUID
    title: str
    content: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()
        
        if self.updated_at is None:
            self.updated_at = datetime.datetime.now()
    
    @staticmethod
    def new(project_id: UUID, title: str, content: str | None = None) -> "Doc":
        return Doc(
            id=uuid4(),
            project_id=project_id,
            title=title,
            content=content
        )


import os
import psycopg2
import psycopg2.extras
from psycopg2.extensions import connection, cursor
psycopg2.extras.register_uuid()

NAME = "pgsql"
PASS = "pgsql"
HOST = "localhost"
PORT = "5432"
DB_NAME = "pgsql"
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



def create(doc: Doc) -> None:
    query = """
    INSERT INTO docs
        (id, project_id, title, content, created_at, updated_at)
    VALUES
        (%s, %s, %s, %s, %s, %s)
    """

    values = (
        doc.id,
        doc.project_id,
        doc.title,
        doc.content,
        doc.created_at,
        doc.updated_at
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)


def main():
    for i in range(1000):
        doc = Doc.new(project_id="0bd367d3-5c2a-4cfa-aa6c-2577416c37e9", title="sample", content="sample")
        create(doc=doc)
        print(i)


if __name__ == "__main__":
    main()