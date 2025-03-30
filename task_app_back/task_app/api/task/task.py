
from logging import getLogger
from uuid import UUID
from fastapi import APIRouter
from .task_schema import (
    TaskCreateRequest,
    TaskCreateResponse,
    TaskGetAllResponse,
    TaskGetResponse,
    TaskUpdateRequest,
    TaskUpdateResponse
)
from ... import domain

logger = getLogger("uvicorn.app")
router = APIRouter()


@router.post(
    "/projects/{project_id}/tasks",
    status_code=201,
    response_model=TaskCreateResponse,
)
def create_task(project_id: UUID, create_request: TaskCreateRequest):
    task_id = domain.task.create(
        project_id=project_id,
        title=create_request.title,
        content=create_request.content,
        status=create_request.status,
        priority=create_request.priority,
        duedate=create_request.duedate
    )
    return TaskCreateResponse(id=task_id)


@router.get(
    "/projects/{project_id}/tasks",
    status_code=200,
    response_model=TaskGetAllResponse
)
def get_tasks(project_id: UUID, status: int = 0):
    tasks = domain.task.get_tasks_with_status(project_id=project_id, status=status)

    tasks = [
        TaskGetResponse(
            id=task.id,
            project_id=task.project_id,
            title=task.title,
            content=task.content,
            status=task.status,
            priority=task.priority,
            duedate=task.duedate
        ) for task in tasks
    ]

    return TaskGetAllResponse(results=tasks, count=len(tasks), next=None, prev=None)


@router.get("/projects/{project_id}/tasks/{task_id}", status_code=200)
def get_task(project_id: UUID, task_id:  UUID):
    task = domain.task.get(project_id=project_id, task_id=task_id)
    return TaskGetResponse(
        id=task.id,
        project_id=task.project_id,
        title=task.title,
        content=task.content,
        status=task.status,
        priority=task.priority,
        duedate=task.duedate
    )


@router.put(
    "/projects/{project_id}/tasks/{task_id}",
    status_code=200,
    response_model=TaskUpdateResponse
)
def update_task(project_id: UUID, task_id:  UUID, update_request: TaskUpdateRequest):
    updated_task = domain.task.update(
        task_id=task_id,
        project_id=project_id,
        title=update_request.title,
        content=update_request.content,
        status=update_request.status,
        priority=update_request.priority,
        duedate=update_request.duedate
    )

    return TaskUpdateResponse(
        id=updated_task.id,
        project_id=updated_task.project_id,
        title=updated_task.title,
        content=updated_task.content,
        status=updated_task.status,
        priority=updated_task.priority,
        duedate=updated_task.duedate
    )


@router.delete("/projects/{project_id}/tasks/{task_id}", status_code=204)
def delete_task(project_id: UUID, task_id:  UUID):
    domain.task.delete(project_id=project_id, task_id=task_id)
