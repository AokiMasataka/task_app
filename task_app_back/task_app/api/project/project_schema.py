from typing import List
from uuid import UUID
from pydantic import BaseModel


class ProjectCreationRequest(BaseModel):
    title: str
    description: str


class ProjectCreationResponse(BaseModel):
    project_id: UUID


class ProjectGetResopnse(BaseModel):
    id: UUID
    title: str
    description: str


class ProjestGetAllResponse(BaseModel):
    results: List[ProjectGetResopnse]
    count: int
    next: None | str
    prev: None | str


class ProjectUpdateRequest(BaseModel):
    title: str
    description: str


class ProjectUpdateResponse(BaseModel):
    id: UUID
    title: str
    description: str