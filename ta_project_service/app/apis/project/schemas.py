from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CreateProjectRequest(BaseModel):
    name: str
    description: str | None = None


class CreateProjectResponse(BaseModel):
    id: str


class GetProjectResponse(BaseModel):
    id: str
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime


class ListProjectsResponse(BaseModel):
    results: list[GetProjectResponse]
    total: int


class UpdateProjectRequest(BaseModel):
    name: str | None = None
    description: str | None = None


class UpdateProjectResponse(CreateProjectResponse):
    pass
