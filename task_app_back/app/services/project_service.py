from uuid import UUID
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from infra import Project, project_repository
from .exceptions import ProjectNotFoundError


def _valiedate_clamps(
    value: int,
    min_value: int | None = None,
    max_value: int | None = None
) -> bool:
    if (min_value is not None) and (value < min_value):
        return False
    if (max_value is not None) and (value > max_value):
        return False
    return True


async def list_projects(
    session: AsyncSession,
    page: int = 1,
    per_page: int = 10,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Project], int]:
    
    if _valiedate_clamps(value=page, min_value=1) is False:
        raise ValueError("Page must be greater than 0.")
    
    if _valiedate_clamps(value=per_page, min_value=1, max_value=100) is False:
        raise ValueError("Limit must be between 1 and 100.")
    
    offset = (page - 1) * per_page

    return await project_repository.list_projects(
        session=session,
        offset=offset,
        limit=per_page,
        sort_by=sort_by,
        sort_order=sort_order
)


async def get_project(
    session: AsyncSession,
    project_id: UUID
) -> Project:
    project = await project_repository.get_project_by_id(
        session=session,
        project_id=project_id
    )
    if project is None:
        raise ProjectNotFoundError("Project not found.")
    return project


async def create_project(
    session: AsyncSession,
    name: str,
    description: str | None = None
) -> UUID:
    if not name:
        raise ValueError("Name is required.")

    project_id = await project_repository.create_project(
        session=session,
        name=name,
        description=description
    )
    return project_id


async def update_project(
    session: AsyncSession,
    project_id: UUID,
    name: str | None = None,
    description: str | None = None
) -> Project:
    try:
        updated_project = await project_repository.update_project(
            session=session,
            project_id=project_id,
            name=name,
            description=description
        )
    except ValueError:
        raise ProjectNotFoundError("Project not found.")
    
    return updated_project


async def delete_project(
    session: AsyncSession,
    project_id: UUID
) -> None:
    await project_repository.delete_project(
        session=session,
        project_id=project_id
    )