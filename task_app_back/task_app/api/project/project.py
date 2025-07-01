from logging import getLogger
from uuid import UUID
from fastapi import APIRouter

from .project_schema import (
    ProjectCreateRequest,
    ProjectCreateResponse,
    ProjectGetResopnse,
    ProjestGetAllResponse,
    ProjectUpdateRequest,
    ProjectUpdateResponse
)

from ... import domain


logger = getLogger("uvicorn.app")
router = APIRouter()

# TODO: Errorハンドリング

@router.post("/projects", status_code=201, response_model=ProjectCreateResponse)
async def create_project(create_request: ProjectCreateRequest):
    project_id = await domain.project.create(create_request.title, create_request.description)
    return ProjectCreateResponse(id=project_id)


@router.get("/projects", status_code=200, response_model=ProjestGetAllResponse)
async def get_projects():
    results = [
        ProjectGetResopnse(
            id=dict_project.id,
            title=dict_project.title,
            description=dict_project.description
        ) for dict_project in await domain.project.get_all()
    ]
    return ProjestGetAllResponse(results=results, count=len(results), next=None, prev=None)


@router.get("/projects/{project_id}", status_code=200, response_model=ProjectGetResopnse)
async def get_project(project_id: UUID):
    project = await domain.project.get(project_id=project_id)
    return ProjectGetResopnse(
        id=project.id,
        title=project.title,
        description=project.description
    )


@router.put("/projects/{project_id}", status_code=200, response_model=ProjectUpdateResponse)
async def update_project(project_id: UUID, update_request: ProjectUpdateRequest):
    updateed_project = await domain.project.update(
        project_id=project_id,
        title=update_request.title,
        description=update_request.description
    )
    return ProjectUpdateResponse(
        id=updateed_project.id,
        title=updateed_project.title,
        description=updateed_project.description
    )


@router.delete("/projects/{project_id}", status_code=204)
async def delete_project(project_id: UUID):
    await domain.project.delete(
        project_id=project_id
    )