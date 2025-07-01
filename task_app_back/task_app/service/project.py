from uuid import UUID
from .utils import AsyncDatabaseConnector
from ..schemas import Project


async def create(project: Project) -> None:
    query = """
    INSERT INTO projects
        (id, title, description, created_at, updated_at)
    VALUES
        ($1, $2, $3, $4, $5)
    """
    values = (
        project.id,
        project.title,
        project.description,
        project.created_at,
        project.updated_at
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)


async def get_all() -> list[dict]:
    query = """
    SELECT
        id, title, description, created_at, updated_at
    FROM
        projects
    """

    async with AsyncDatabaseConnector() as conn:
        results = await conn.fetch(query)

    return [dict(result) for result in results]


async def get(project_id: UUID) -> dict:
    query = """
    SELECT
        id, title, description, created_at, updated_at
    FROM
        projects
    WHERE
        id = $1
    """
    values = (project_id,)

    async with AsyncDatabaseConnector() as cur:
        result = await cur.fetchrow(query, *values)

    return dict(result)


async def update(project: Project) -> None:
    query = """
    UPDATE
        projects
    SET
        title = $1,
        description = $2,
        updated_at = $3
    WHERE
        id = $4
    """
    values = (
        project.title,
        project.description,
        project.updated_at,
        project.id
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)


async def delete(project_id: UUID) -> None:
    query = """
    DELETE FROM
        projects
    WHERE
        id = $1
    """
    values = (project_id, )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)