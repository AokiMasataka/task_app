from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CreateDocumentRequest(BaseModel):
    title: str
    content: str


class CreateDocumentResponse(BaseModel):
    id: str


class GetDocumentResponse(BaseModel):
    id: str
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


class ListDocumentsResponse(BaseModel):

    class DocumentItem(BaseModel):
        id: str
        title: str
        created_at: datetime
        updated_at: datetime
    
    results: list[DocumentItem]
    total: int
    page: int
    per_page: int


class UpdateDocumentRequest(BaseModel):
    title: str | None = None
    content: str | None = None


class UpdateDocumentResponse(CreateDocumentResponse):
    pass