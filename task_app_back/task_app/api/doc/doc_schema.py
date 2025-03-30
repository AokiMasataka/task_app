from typing import List, Union
from uuid import UUID
from pydantic import BaseModel


class BaseDoc(BaseModel):
    title: str
    content: Union[str, None] = None


class DocCreateRequest(BaseDoc):
    pass


class DocCreateResponse(BaseModel):
    id: UUID


class DocGetResponse(BaseDoc):
    id: UUID
    project_id: UUID


class DocGetAllResponse(BaseModel):
    results: List[DocGetResponse]
    count: int
    next: Union[str, None] = None
    prev: Union[str, None] = None


class DocUpdateRequest(BaseDoc):
    pass


class DocUpdateResponse(BaseDoc):
    id: UUID
    project_id: UUID