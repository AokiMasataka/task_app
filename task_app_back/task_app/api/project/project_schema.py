from typing import List, Union
from uuid import UUID
from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):
    title: str
    description: Union[str, None]


class ProjectCreateResponse(BaseModel):
    id: UUID


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
    description: Union[str, None]


class ProjectUpdateResponse(BaseModel):
    id: UUID
    title: str
    description: str