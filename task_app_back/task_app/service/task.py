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


def get_tasks_with_status(project_id: UUID, status: int = None) -> list[dict]:
    query = """
    SELECT
        id, title, content, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        project_id = %s AND status = %s
    """
    values = (project_id, status)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        rows = cur.fetchall()

    tasks = [dict(row) for row in rows]

    return tasks


def get(project_id: UUID, task_id: UUID):
    query = """
    SELECT
        id, title, content, status, priority, duedate, created_at, updated_at
    FROM
        tasks
    WHERE
        project_id = %s AND id = %s
    """
    values = (project_id, task_id)

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)
        row = cur.fetchone()

    task = dict(row)
    return task


def create(task: Task):
    
    query = """
    INSERT INTO tasks
        (id, project_id, title, content, status, priority, duedate, created_at, updated_at)
    VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s)
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
        project_id = %s AND id = %s
    """
    values = (
        task.title,
        task.content,
        task.status,
        task.priority,
        task.duedate,
        task.updated_at,
        task.project_id,
        task.id
    )

    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)


def delete(project_id: UUID, task_id: UUID):
    query = """
    DELETE FROM
        tasks
    WHERE
        project_id = %s AND id = %s
    """
    values = (project_id,  task_id)
    
    with DatabaseConnector() as cur:
        cur.execute(query=query, vars=values)