from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    title: str
    content: str | None = None
    priority: int = 0
    status: int = 0
    duedate: datetime | None = None


class CreateTaskResponse(BaseModel):
    id: str


class GetTaskResponse(BaseModel):
    id: str
    title: str
    content: str | None = None
    priority: int
    status: int
    duedate: datetime | None = None
    created_at: datetime
    updated_at: datetime


class ListTasksResponse(BaseModel):

    class TaskItem(BaseModel):
        id: str
        title: str
        priority: int
        status: int
        duedate: datetime | None = None
        created_at: datetime
        updated_at: datetime
    
    results: list[TaskItem]
    total: int
    page: int
    per_page: int


class UpdateTaskRequest(BaseModel):
    title: str | None = None
    content: str | None = None
    priority: int | None = None
    status: int | None = None
    duedate: datetime | None = None


class UpdateTaskResponse(CreateTaskResponse):
    pass
