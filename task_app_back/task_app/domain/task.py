from typing import List, Union
from uuid import UUID
from ..schemas import Task
from ..service import task as task_service


def create(
    project_id: UUID,
    title: str,
    content: str,
    status: str,
    priority: int,
    duedate: Union[str, None] = None
) -> UUID:
    new_task = Task.new(
        project_id=project_id,
        title=title,
        content=content,
        status=status,
        priority=priority,
        duedate=duedate
    )

    task_service.create(task=new_task)
    return new_task.uuid


def get_tasks_with_status(project_id: UUID, status: int) -> List[Task]:
    tasks = task_service.get_tasks_with_status(project_id=project_id, status=status)
    tasks = [Task(**task) for task in tasks]
    return tasks


def get(project_id: UUID, task_id: UUID) -> Task:
    task = task_service.get(project_id=project_id, task_id=task_id)
    task = Task(**task)
    return task


def update(task: Task) -> None:
    task_service.update(task=task)


def delete(project_id: UUID, task_id: UUID) -> None:
    task_service.delete(project_id=project_id, task_id=task_id)