from typing import List
from uuid import UUID
from .utils import AsyncDatabaseConnector
from ..schemas import Task


async def get_tasks_with_status(project_id: UUID, status: int, sort_key: str) -> List[dict]:
    if "priority" not in ["priority", "duedate"]:
        return []
    
    query = f"""
    SELECT
        id, title, content, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        project_id = $1 AND status = $2
    ORDER BY {sort_key} DESC
    """
    values = (project_id, status)

    async with AsyncDatabaseConnector() as conn:
        results = await conn.fetch(query, *values)
    
    return [dict(result) for result in results]


async def get(task_id: UUID) -> dict:
    query = """
    SELECT
        id, project_id, title, content, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        id = $1
    """
    values = (task_id, )

    async with AsyncDatabaseConnector() as conn:
        result = await conn.fetchrow(query, *values)
    return dict(result)


async def create(task: Task) -> None:
    query = """
    INSERT INTO tasks
        (id, project_id, title, content, status, priority, duedate, created_at, updated_at)
    VALUES
        ($1, $2, $3, $4, $5, $6, $7, $8, $9)
    """
    values = (
        task.id,
        task.project_id,
        task.title,
        task.content,
        task.status,
        task.priority,
        task.duedate,
        task.created_at,
        task.updated_at
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)

async def update(task: Task) -> None:
    query = """
    UPDATE
        tasks
    SET
        title = $1,
        content = $2,
        status = $3,
        priority = $4,
        duedate = $5,
        updated_at = $6
    WHERE
        id = $7
    """
    values = (
        task.title,
        task.content,
        task.status,
        task.priority,
        task.duedate,
        task.updated_at,
        task.id
    )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)


async def delete(task_id: UUID) -> None:
    query = """
    DELETE FROM
        tasks
    WHERE
        id = $1
    """
    values = (task_id, )

    async with AsyncDatabaseConnector() as conn:
        await conn.execute(query, *values)