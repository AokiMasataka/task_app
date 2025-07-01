from typing import List
from uuid import UUID
from .utils import AsyncDatabaseConnector
from ..schemas import Doc


async def get_all(project_id: UUID) -> List[dict]:
    query = """
    SELECT
        id, title, content, created_at, updated_at
    FROM
        docs
    WHERE
        project_id = $1
    """

    values = (project_id, )
    async with AsyncDatabaseConnector() as conn:
        results = await conn.fetch(query, *values)
    
    return [dict(result) for result in results]


async def get(doc_id: UUID) -> dict:
    query = """
    SELECT
        id, project_id, title, content, created_at, updated_at
    FROM
        docs
    WHERE
        id = $1
    """

    values = (doc_id, )

    async with AsyncDatabaseConnector() as conn:
        result = await conn.fetchrow(query, *values)
    return dict(result)


async def create(doc: Doc) -> None:
    query = """
    INSERT INTO docs
        (id, project_id, title, content, created_at, updated_at)
    VALUES
        ($1, $2, $3, $4, $5, $6)
    """

    values = (
        doc.id,
        doc.project_id,
        doc.title,
        doc.content,
        doc.created_at,
        doc.updated_at
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)


async def update(doc: Doc) -> None:
    query = """
    UPDATE
        docs
    SET
        title = $1,
        content = $2,
        updated_at = $3
    WHERE
        id = $4
    """

    values = (
        doc.title,
        doc.content,
        doc.updated_at,
        doc.id
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)


async def delete(doc_id: UUID) -> None:
    query = """
    DELETE FROM
        docs
    WHERE
        id = $1
    """

    values = (doc_id, )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)