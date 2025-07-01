from typing import List, Union
from uuid import UUID
from ..schemas import Task
from ..service import task as task_service


async def create(
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

    await task_service.create(task=new_task)
    return new_task.id


async def get_tasks_with_status(project_id: UUID, status: int, sort_key: str) -> List[Task]:
    tasks = await task_service.get_tasks_with_status(
        project_id=project_id,
        status=status,
        sort_key=sort_key
    )
    tasks = [Task(**task, project_id=project_id) for task in tasks]
    return tasks


async def get(task_id: UUID) -> Task:
    task = await task_service.get(task_id=task_id)
    task = Task(**task)
    return task


async def update(
    task_id: UUID,
    project_id: UUID,
    title: str,
    content: str,
    status: str,
    priority: int,
    duedate: Union[str, None] = None
) -> Task:
    updated_task = Task(
        id=task_id,
        project_id=project_id,
        title=title,
        content=content,
        status=status,
        priority=priority,
        duedate=duedate
    )
    await task_service.update(task=updated_task)
    return updated_task


async def delete(task_id: UUID) -> None:
    await task_service.delete(task_id=task_id)
