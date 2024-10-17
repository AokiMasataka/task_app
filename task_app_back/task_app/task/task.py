import datetime

from .model import (
    Task,
    get_tasks,
    get_tasks_with_status,
    get_task,
    create_task,
    update_task,
    delete_task
)


def create(title: str, content: str) -> Task:
    task = Task(title=title, content=content)
    create_task(task=task)

    return task


def get_all() -> list[dict]:
    tasks = get_tasks()
    return tasks

def get_with_status(status=1) -> list[dict]:
    tasks = get_tasks_with_status(status=status)
    return tasks

def get(task_id: str) -> Task:
    task = get_task(uuid=task_id)
    return task


def update(task_id: str, title: str, content: str):
    task = Task(
        title=title,
        content=content,
        uuid=task_id,
        updated_at=datetime.datetime.now()
    )
    update_task(task=task)


def delete(task_id: str) -> None:
    delete_task(uuid=task_id)

