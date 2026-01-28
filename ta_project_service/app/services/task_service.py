from uuid import UUID
from typing import Literal
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from infra import Task, task_repository
from .exceptions import TaskNotFoundError

from .project_service import _valiedate_clamps


async def list_tasks(
    session: AsyncSession,
    project_id: UUID,
    status: int | None = None,
    page: int = 1,
    per_page: int = 10,
    sort_by: Literal["created_at", "updated_at", "priority", "status"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Task], int]:
    
    if _valiedate_clamps(value=page, min_value=1) is False:
        raise ValueError("Page must be greater than 0.")
    
    if _valiedate_clamps(value=per_page, min_value=1, max_value=100) is False:
        raise ValueError("Per page must be between 1 and 100.")
    
    offset = (page - 1) * per_page

    return await task_repository.list_tasks(
        session=session,
        project_id=project_id,
        status=status,
        offset=offset,
        limit=per_page,
        sort_by=sort_by,
        sort_order=sort_order
)


async def get_task(
    session: AsyncSession,
    task_id: UUID
) -> Task:
    task = await task_repository.get_task_by_id(
        session=session,
        task_id=task_id
    )
    if task is None:
        raise TaskNotFoundError("Task not found.")
    return task


async def create_task(
    session: AsyncSession,
    project_id: UUID,
    title: str,
    content: str | None = None,
    priority: int = 0,
    status: int = 0,
    duedate: datetime | None = None
) -> UUID:
    return await task_repository.create_task(
        session=session,
        project_id=project_id,
        title=title,
        content=content,
        priority=priority,
        status=status,
        duedate=duedate
    )


async def update_task(
    session: AsyncSession,
    task_id: UUID,
    title: str | None = None,
    content: str | None = None,
    priority: int | None = None,
    status: int | None = None,
    duedate: datetime | None = None
) -> Task:

    try:
        updated_task = await task_repository.update_task(
            session=session,
            task_id=task_id,
            title=title,
            content=content,
            priority=priority,
            status=status,
            duedate=duedate
        )
    except ValueError:
        raise TaskNotFoundError("Task not found.")
    
    return updated_task


async def delete_task(
    session: AsyncSession,
    task_id: UUID
) -> None:
    await task_repository.delete_task(
        session=session,
        task_id=task_id
    )
    