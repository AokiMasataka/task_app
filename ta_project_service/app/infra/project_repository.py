from uuid import UUID, uuid4
from typing import Literal

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Project


__all__ = [
    "list_projects",
    "get_project_by_id",
    "create_project",
    "update_project",
    "delete_project",
]


async def list_projects(
    session: AsyncSession,
    offset: int,
    limit: int,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Project], int]:
    stmt = select(Project)

    sort_column = Project.updated_at if sort_by == "updated_at" else Project.created_at
    if sort_order == "desc":
        stmt = stmt.order_by(desc(sort_column))
    else:
        stmt = stmt.order_by(sort_column)
    
    # Get total count
    count_stmt = select(func.count()).select_from(Project)
    result = await session.execute(count_stmt)
    total = result.scalar_one()
    
    stmt = stmt.offset(offset).limit(limit)

    # Execute query
    result = await session.execute(stmt)
    project = result.scalars().all()

    return project, total


async def get_project_by_id(
    session: AsyncSession,
    project_id: UUID
) -> Project | None:
    stmt = select(Project).where(Project.id == project_id)
    result = await session.execute(stmt)
    project = result.scalar_one_or_none()
    return project


async def create_project(
    session: AsyncSession,
    name: str,
    description: str | None = None
) -> UUID:
    uid = uuid4()
    project = Project(
        id=uid,
        name=name,
        description=description
    )
    session.add(project)
    await session.commit()
    return uid


async def update_project(
    session: AsyncSession,
    project_id: UUID,
    name: str | None = None,
    description: str | None = None
) -> Project:
    project = await get_project_by_id(
        session=session, project_id=project_id
    )
    if not project:
        raise ValueError("Project not found.")
    
    if name is not None:
        project.name = name
    if description is not None:
        project.description = description
    
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project


async def delete_project(session: AsyncSession, project_id: UUID) -> None:
    project = await session.get(Project, project_id)
    if not project:
        raise ValueError("Project not found.")

    await session.delete(project)
    await session.commit()