from typing import Union, List
from uuid import UUID
from datetime import date
from pydantic import BaseModel


class TaskCreateRequest(BaseModel):
    title: str
    content: str
    status: int
    priority: int
    duedate: Union[date, None] = None


class TaskCreateResponse(BaseModel):
    task_id: UUID


class TaskGetResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    content: str
    status: int
    priority: int
    duedate: Union[date, None] = None


class TaskGetAllResponse(BaseModel):
    results: List[TaskGetResponse]
    count: int
    next: None | str
    prev: None | str


class TaskUpdateRequest(BaseModel):
    title: str
    content: str
    status: int
    priority: int
    duedate: Union[date, None] = None


class TaskUpdateResponse(BaseModel):
    id: UUID
    project_id: UUID
    title: str
    content: str
    status: int
    priority: int
    duedate: Union[date, None] = None