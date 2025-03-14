from logging import getLogger
from uuid import UUID
from fastapi import APIRouter

from .project_schema import (
    ProjectCreationRequest,
    ProjectCreationResponse,
    ProjectGetResopnse,
    ProjestGetAllResponse,
    ProjectUpdateRequest,
    ProjectUpdateResponse
)

from ... import domain


logger = getLogger("uvicorn.app")
app = APIRouter()

# TODO: Errorハンドリング

@app.post("/projects", status_code=201, response_model=ProjectCreationResponse)
def create_project(create_request: ProjectCreationRequest):
    project_id = domain.project.create(create_request.title, create_request.description)
    return ProjectCreationResponse(project_id=project_id)


@app.get("/projects", status_code=200, response_model=ProjestGetAllResponse)
def get_projects():
    results = [
        ProjectGetResopnse(
            id=dict_project.uuid,
            title=dict_project.title,
            description=dict_project.description
        ) for dict_project in domain.project.get_all()
    ]
    return ProjestGetAllResponse(results=results, count=len(results), next=None, prev=None)


@app.get("/projects/{project_id}", status_code=200, response_model=ProjectGetResopnse)
def get_project(project_id: UUID):
    project = domain.project.get(project_id=project_id)
    return ProjectGetResopnse(
        id=project.uuid,
        title=project.title,
        description=project.description
    )


@app.put("/projects/{project_id}", status_code=200, response_model=ProjectUpdateResponse)
def update_project(project_id: UUID, update_request: ProjectUpdateRequest):
    updateed_project = domain.project.update(
        project_id=project_id,
        title=update_request.title,
        description=update_request.description
    )
    return ProjectUpdateResponse(
        id=updateed_project.uuid,
        title=updateed_project.title,
        description=updateed_project.description
    )


@app.delete("/projects/{project_id}", status_code=204)
def delete_project(project_id: UUID):
    domain.project.delete(
        project_id=project_id
    )