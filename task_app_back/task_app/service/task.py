from uuid import UUID
from ..schemas import Task
from .utils import DatabaseConnector


__all__ = [
    "get",
    "get_tasks_with_status",
    "create",
    "update",
    "delete"
]


def get_tasks_with_status(status: int = None) -> list[dict]:
    query = """
    SELECT
        title, content, id, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        status = %s
    """
    values = (status, )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        rows = cur.fetchall()

    tasks = [dict(row) for row in rows]

    return tasks


def get(task_id: UUID):
    query = """
    SELECT
        title, content, id, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        id = %s
    """
    values = (task_id,)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        row = cur.fetchone()

    task = dict(row)
    return task


def create(task: Task):
    
    query = """
    INSERT INTO tasks
        (id, title, content, status, priority, duedate, created_at, updated_at)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        task.uuid,
        task.title,
        task.content,
        task.status,
        task.priority,
        task.duedate,
        task.created_at,
        task.updated_at
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)


def update(task: Task):
    query = """
    UPDATE
        tasks
    SET
        title = %s,
        content = %s,
        status = %s,
        priority = %s,
        duedate = %s,
        updated_at = %s
    WHERE
        id = %s
    """
    values = (
        task.title,
        task.content,
        task.status,
        task.priority,
        task.duedate,
        task.updated_at,
        task.uuid
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)


def delete(task_id: UUID):
    query = """
    DELETE FROM
        tasks
    WHERE
        id = %s
    """
    values = (task_id, )
    
    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)