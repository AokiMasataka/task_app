import base64
from uuid import UUID
from typing import Literal

from fastapi import APIRouter

from core import get_logger
from services import project_service
from ..deps import DBSessionDeps
from .schemas import (
    CreateProjectRequest,
    CreateProjectResponse,
    GetProjectResponse,
    ListProjectsResponse,
    UpdateProjectRequest,
    UpdateProjectResponse
)




logger = get_logger(__name__)
project_router = APIRouter(tags=["projects"])


@project_router.get("/projects", response_model=ListProjectsResponse)
async def list_projects(
    page: int = 1,
    per_page: int = 10,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc",
    db_session=DBSessionDeps
) -> ListProjectsResponse:
    projects, total = await project_service.list_projects(
        session=db_session,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        sort_order=sort_order
    )

    logger.info("listed projects", total=total, page=page, per_page=per_page)
    return ListProjectsResponse(
        total=total,
        results=[
            GetProjectResponse(
                id=base64.urlsafe_b64encode(project.id.bytes).decode().rstrip("="),
                name=project.name,
                description=project.description,
                created_at=project.created_at,
                updated_at=project.updated_at
            )
            for project in projects
        ]
    )


@project_router.post(
    "/projects",
    status_code=201,
    response_model=CreateProjectResponse
)
async def create_project(
    request: CreateProjectRequest,
    db_session=DBSessionDeps
) -> CreateProjectResponse:
    project_id = await project_service.create_project(
        session=db_session,
        name=request.name,
        description=request.description
    )
    logger.info("created project", project_id=str(project_id), project_name=request.name)
    return CreateProjectResponse(
        id=base64.urlsafe_b64encode(project_id.bytes).decode().rstrip("=")
    )


@project_router.get(
    "/projects/{project_id}",
    response_model=GetProjectResponse
)
async def get_project(
    project_id: str,
    db_session=DBSessionDeps
) -> GetProjectResponse:
    project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    project = await project_service.get_project(
        session=db_session,
        project_id=project_id,
    )
    logger.info("fetched project", project_id=str(project_id))
    return GetProjectResponse(
        id=base64.urlsafe_b64encode(project.id.bytes).decode().rstrip("="),
        name=project.name,
        description=project.description,
        created_at=project.created_at,
        updated_at=project.updated_at
    )


@project_router.put(
    "/projects/{project_id}",
    response_model=UpdateProjectResponse,
)
async def update_project(
    project_id: str,
    request: UpdateProjectRequest,
    db_session=DBSessionDeps
) -> UpdateProjectResponse:
    project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    updated_project = await project_service.update_project(
        session=db_session,
        project_id=project_id,
        name=request.name,
        description=request.description
    )
    logger.info("updated project", project_id=str(project_id))

    return UpdateProjectResponse(
        id=base64.urlsafe_b64encode(updated_project.id.bytes).decode().rstrip("=")
    )


@project_router.delete("/projects/{project_id}", status_code=204)
async def delete_project(
    project_id: str,
    db_session=DBSessionDeps
) -> None:
    logger.info("deleting project", project_id=str(project_id))
    project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    await project_service.delete_project(
        session=db_session,
        project_id=project_id,
    )
