
from logging import getLogger
from uuid import UUID
from fastapi import APIRouter
from .task_schema import (
    TaskCreateRequest,
    TaskCreateResponse,
    TaskGetAllResponse,
    TaskUpdateRequest
)
from ... import domain

logger = getLogger("uvicorn.app")
app = APIRouter()


@app.post(
    "/project/{project_id}/tasks",
    status_code=201,
    response_model=TaskCreateResponse,
)
def create_task(project_id: UUID, create_request: TaskCreateRequest):
    cretaed_task_id = domain.task.create(
        project_id=project_id,
        title=create_request.title,
        content=create_request.content,
        status=create_request.status,
        priority=create_request.priority,
        duedate=create_request.duedate
    )
    return TaskCreateResponse(task_id=cretaed_task_id)


@app.get(
    "/project/{project_id}/tasks",
    status_code=200,
    response_model=TaskGetAllResponse
)
def get_tasks(project_id: UUID, status: int = 0):
    pass


@app.get("/project/{project_id}/tasks/{task_id}", status_code=200)
def get_task(project_id: UUID, task_id:  UUID):
    pass


@app.put("/project/{project_id}/tasks/{task_id}", status_code=200)
def update_task(project_id: UUID, task_id:  UUID, create_request: TaskUpdateRequest):
    pass


@app.delete("/project/{project_id}/tasks/{task_id}", status_code=200)
def delete_task(project_id: UUID, task_id:  UUID):
    pass
