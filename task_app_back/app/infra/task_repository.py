from uuid import UUID, uuid4
from typing import Literal
from datetime import datetime

from sqlalchemy import desc, func, select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Task


async def list_tasks(
    session: AsyncSession,
    project_id: UUID,
    status: int,
    offset: int,
    limit: int,
    sort_by: Literal["created_at", "updated_at", "priority", "status"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Task], int]:
    if status is not None:
        w = and_(Task.project_id == project_id, Task.status == status)
    else:
        w = Task.project_id == project_id

    stmt = select(Task).where(w)

    sort_column = {
        "created_at": Task.created_at,
        "updated_at": Task.updated_at,
        "priority": Task.priority,
        "status": Task.status
    }[sort_by]

    if sort_order == "desc":
        stmt = stmt.order_by(desc(sort_column))
    else:
        stmt = stmt.order_by(sort_column)

    # Get total count
    count_stmt = select(func.count()).select_from(Task).where(Task.project_id == project_id)
    result = await session.execute(count_stmt)
    total = result.scalar_one()

    stmt = stmt.offset(offset).limit(limit)

    # Execute query
    result = await session.execute(stmt)
    tasks = result.scalars().all()

    return tasks, total


async def get_task_by_id(
    session: AsyncSession,
    task_id: UUID
) -> Task | None:
    stmt = select(Task).where(Task.id == task_id)
    result = await session.execute(stmt)
    task = result.scalar_one_or_none()
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
    uid = uuid4()
    new_task = Task(
        id=uid,
        project_id=project_id,
        title=title,
        content=content,
        priority=priority,
        status=status,
        duedate=duedate
    )
    session.add(new_task)
    await session.commit()
    return uid


async def update_task(
    session: AsyncSession,
    task_id: UUID,
    title: str | None = None,
    content: str | None = None,
    priority: int | None = None,
    status: int | None = None,
    duedate: datetime | None = None
) -> Task:
    task = await get_task_by_id(session=session, task_id=task_id)
    if not task:
        raise ValueError("Task not found.")

    if title is not None:
        task.title = title
    if content is not None:
        task.content = content
    if priority is not None:
        task.priority = priority
    if status is not None:
        task.status = status
    if duedate is not None:
        task.duedate = duedate

    await session.commit()
    return task


async def delete_task(session: AsyncSession, task_id: UUID) -> None:
    task = await session.get(Task, task_id)
    if not task:
        raise ValueError("Task not found.")
    await session.delete(task)
    await session.commit()