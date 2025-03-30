from typing import List
from uuid import UUID
from .utils import DatabaseConnector
from ..schemas import Doc


__all__ = [
    "get",
    "create",
    "update",
    "delete"
]


def get_all(project_id: UUID) -> List[dict]:
    query = """
    SELECT
        id, title, content, created_at, updated_at
    FROM
        docs
    WHERE
        project_id = %s
    """

    values = (project_id, )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        rows = cur.fetchall()
    
    docs = [dict(row) for row in rows]
    return docs


def get(project_id: UUID, doc_id: UUID) -> dict:
    query = """
    SELECT
        id, title, content, created_at, updated_at
    FROM
        docs
    WHERE
        project_id = %s AND id = %s
    """

    values = (project_id, doc_id)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        row = cur.fetchone()
    
    docs = dict(row)
    return docs


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


def update(doc: Doc) -> None:
    query = """
    UPDATE
        docs
    SET
        id = %s,
        project_id = %s,
        title = %s,
        content = %s,
        created_at = %s,
        updated_at = %s
    """

    values = (
        doc.id,
        doc.project_id,
        doc.title,
        doc.content,
        doc.created_at,
        doc.updated_at
    )

    with DatabaseConnector()  as cur:
        cur.execute(query=query, vars=values)


def delete(project_id: UUID, doc_id: UUID) -> None:
    query = """
    DELETE FROM
        tasks
    WHERE
        project_id = %s AND id = %s
    """

    values = (project_id, doc_id)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)

