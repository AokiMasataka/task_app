import base64
from uuid import UUID
from fastapi import APIRouter

from core import get_logger
from services import task_service
from ..deps import DBSessionDep
from .schemas import (
    CreateTaskRequest,
    CreateTaskResponse,
    GetTaskResponse,
    ListTasksResponse,
    UpdateTaskRequest,
    UpdateTaskResponse
)


logger = get_logger(__name__)
task_router = APIRouter(tags=["tasks"], prefix="/api")


@task_router.get(
    "/projects/{project_id}/tasks",
    response_model=ListTasksResponse
)
async def list_tasks(
    db_session: DBSessionDep,
    project_id: str,
    status: int | None = None,
    page: int = 1,
    per_page: int = 10,
    sort_by: str = "updated_at",
    sort_order: str = "desc",
) -> ListTasksResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    
    tasks, total = await task_service.list_tasks(
        session=db_session,
        project_id=decoded_project_id,
        status=status,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        sort_order=sort_order
    )
    
    logger.info(
        "listed tasks",
        project_id=str(decoded_project_id),
        total=total,
        page=page,
        per_page=per_page
    )

    return ListTasksResponse(
        total=total,
        page=page,
        per_page=per_page,
        results=[
            ListTasksResponse.TaskItem(
                id=base64.urlsafe_b64encode(task.id.bytes).decode().rstrip("="),
                title=task.title,
                priority=task.priority,
                status=task.status,
                duedate=task.duedate,
                created_at=task.created_at,
                updated_at=task.updated_at
            )
            for task in tasks
        ]
    )


@task_router.post(
    "/projects/{project_id}/tasks",
    status_code=201,
    response_model=CreateTaskResponse
)
async def create_task(
    db_session: DBSessionDep,
    project_id: str,
    request: CreateTaskRequest,
) -> CreateTaskResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    
    task_id = await task_service.create_task(
        session=db_session,
        project_id=decoded_project_id,
        title=request.title,
        content=request.content,
        priority=request.priority,
        status=request.status,
        duedate=request.duedate
    )
    
    logger.info(
        "created task",
        project_id=str(decoded_project_id),
        task_id=str(task_id),
        task_title=request.title
    )
    
    return CreateTaskResponse(
        id=base64.urlsafe_b64encode(task_id.bytes).decode().rstrip("=")
    )


@task_router.get(
    "/projects/{project_id}/tasks/{task_id}",
    response_model=GetTaskResponse
)
async def get_task(
    db_session: DBSessionDep,
    project_id: str,
    task_id: str,
) -> GetTaskResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_task_id = UUID(bytes=base64.urlsafe_b64decode(task_id + "=="))

    task = await task_service.get_task(
        session=db_session,
        task_id=decoded_task_id
    )
    
    logger.info(
        "fetched task",
        project_id=str(decoded_project_id),
        task_id=str(task.id)
    )
    
    return GetTaskResponse(
        id=base64.urlsafe_b64encode(task.id.bytes).decode().rstrip("="),
        title=task.title,
        content=task.content,
        priority=task.priority,
        status=task.status,
        duedate=task.duedate,
        created_at=task.created_at,
        updated_at=task.updated_at
    )


@task_router.put(
    "/projects/{project_id}/tasks/{task_id}",
    response_model=UpdateTaskResponse,
)
async def update_task(
    db_session: DBSessionDep,
    project_id: str,
    task_id: str,
    request: UpdateTaskRequest,
) -> UpdateTaskResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_task_id = UUID(bytes=base64.urlsafe_b64decode(task_id + "=="))

    updated_task = await task_service.update_task(
        session=db_session,
        task_id=decoded_task_id,
        title=request.title,
        content=request.content,
        priority=request.priority,
        status=request.status,
        duedate=request.duedate
    )
    logger.info(
        "updated task",
        project_id=str(decoded_project_id),
        task_id=str(task_id)
    )
    
    return UpdateTaskResponse(
        id=base64.urlsafe_b64encode(updated_task.id.bytes).decode().rstrip("=")
    )


@task_router.delete("/projects/{project_id}/tasks/{task_id}", status_code=204)
async def delete_task(
    db_session: DBSessionDep,
    project_id: str,
    task_id: str,
) -> None:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_task_id = UUID(bytes=base64.urlsafe_b64decode(task_id + "=="))

    logger.info(
        "deleting task",
        project_id=str(decoded_project_id),
        task_id=str(task_id)
    )
    
    await task_service.delete_task(
        session=db_session,
        task_id=decoded_task_id
    )