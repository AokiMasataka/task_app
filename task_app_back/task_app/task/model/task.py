from .struct import Task, Status
from .utils import query_execute


__all__ = [
    "get_tasks",
    "get_task",
    "get_tasks_with_status",
    "create_task",
    "update_task",
    "delete_task"
]


def get_tasks() -> list[dict]:
    query = """
    SELECT
        title, content, id, status, created_at, updated_at
    FROM
        tasks
    """
    rows = query_execute(query=query, fetch="fetchall")
    tasks = [dict(row) for row in rows]

    return tasks


def get_tasks_with_status(status: int = None) -> list[dict]:
    query = """
    SELECT
        title, content, id, status, created_at, updated_at
    FROM
        tasks
    WHERE
        status = %s
    """
    values = (status, )

    rows = query_execute(query=query, values=values, fetch="fetchall")
    tasks = [dict(row) for row in rows]

    return tasks


def get_task(uuid):
    query = """
    SELECT
        title, content, id, status, created_at, updated_at
    FROM
        tasks
    WHERE
        id = %s
    """
    values = (uuid,)

    row = query_execute(query=query, values=values, fetch="fetchone")
    task = dict(row)
    return task


def create_task(task: Task):
    query = """
    INSERT INTO tasks
        (id, title, content, status, created_at, updated_at)
    VALUES
        (%s, %s, %s, %s, %s, %s)
    """
    values = (
        str(task.uuid),
        task.title,
        task.content,
        task.status,
        task.created_at,
        task.updated_at
    )

    query_execute(query=query, values=values)


def update_task(task: Task):
    query = """
    UPDATE
        tasks
    SET
        title = %s, content = %s, status = %s, updated_at = %s
    WHERE
        id = %s
    """
    values = (
        task.title,
        task.content,
        task.status,
        task.updated_at,
        str(task.uuid)
    )

    query_execute(query=query, values=values)


def delete_task(uuid):
    query = """
    DELETE FROM
        tasks
    WHERE
        id = %s
    """
    values = (uuid, )
    query_execute(query=query, values=values)