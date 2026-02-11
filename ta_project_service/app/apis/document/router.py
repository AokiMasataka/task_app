import base64
from uuid import UUID
from typing import Literal

from fastapi import APIRouter

from core import get_logger
from services import document_service
from .schemas import (
    CreateDocumentRequest,
    CreateDocumentResponse,
    GetDocumentResponse,
    ListDocumentsResponse,
    UpdateDocumentRequest,
    UpdateDocumentResponse
)
from ..deps import DBSessionDep

logger = get_logger(__name__)
document_router = APIRouter(tags=["documents"], prefix="/api")


@document_router.get("/projects/{project_id}/docs", response_model=ListDocumentsResponse)
async def list_documents(
    db_session: DBSessionDep,
    project_id: str,
    page: int = 1,
    per_page: int = 10,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc",
) -> ListDocumentsResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))

    documents, total = await document_service.list_documents(
        session=db_session,
        project_id=decoded_project_id,
        page=page,
        per_page=per_page,
        sort_by=sort_by,
        sort_order=sort_order
    )
    
    logger.info(
        "listed documents",
        project_id=str(decoded_project_id),
        total=total,
        page=page,
        per_page=per_page
    )
    
    return ListDocumentsResponse(
        total=total,
        page=page,
        per_page=per_page,
        results=[
            ListDocumentsResponse.DocumentItem(
                id=base64.urlsafe_b64encode(document.id.bytes).decode().rstrip("="),
                title=document.title,
                created_at=document.created_at,
                updated_at=document.updated_at
            )
            for document in documents
        ]
    )


@document_router.post(
    "/projects/{project_id}/docs",
    status_code=201,
    response_model=CreateDocumentResponse
)
async def create_document(
    db_session: DBSessionDep,
    project_id: str,
    request: CreateDocumentRequest,
) -> CreateDocumentResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))

    document_id = await document_service.create_document(
        session=db_session,
        project_id=decoded_project_id,
        title=request.title,
        content=request.content
    )
    logger.info("created document", project_id=str(decoded_project_id), document_id=str(document_id))
    return CreateDocumentResponse(
        id=base64.urlsafe_b64encode(document_id.bytes).decode().rstrip("=")
    )



@document_router.get(
    "/projects/{project_id}/docs/{document_id}",
    response_model=GetDocumentResponse
)
async def get_document(
    db_session: DBSessionDep,
    project_id: str,
    document_id: str,
) -> GetDocumentResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_document_id = UUID(bytes=base64.urlsafe_b64decode(document_id + "=="))

    document = await document_service.get_document(
        session=db_session,
        document_id=decoded_document_id
    )
    logger.info("retrieved document", project_id=str(decoded_project_id), document_id=str(document.id))
    return GetDocumentResponse(
        id=base64.urlsafe_b64encode(document.id.bytes).decode().rstrip("="),
        title=document.title,
        content=document.content,
        created_at=document.created_at,
        updated_at=document.updated_at
    )


@document_router.put(
    "/projects/{project_id}/docs/{document_id}",
    response_model=UpdateDocumentResponse
)
async def update_document(
    db_session: DBSessionDep,
    project_id: str,
    document_id: str,
    request: UpdateDocumentRequest,
) -> UpdateDocumentResponse:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_document_id = UUID(bytes=base64.urlsafe_b64decode(document_id + "=="))

    updated_document = await document_service.update_document(
        session=db_session,
        document_id=decoded_document_id,
        title=request.title,
        content=request.content
    )
    logger.info(
        "updated document",
        project_id=str(decoded_project_id),
        document_id=str(updated_document.id)
    )

    return UpdateDocumentResponse(
        id=base64.urlsafe_b64encode(updated_document.id.bytes).decode().rstrip("=")
    )


@document_router.delete("/projects/{project_id}/docs/{document_id}", status_code=204)
async def delete_document(
    db_session: DBSessionDep,
    project_id: str,
    document_id: str,
) -> None:
    decoded_project_id = UUID(bytes=base64.urlsafe_b64decode(project_id + "=="))
    decoded_document_id = UUID(bytes=base64.urlsafe_b64decode(document_id + "=="))

    await document_service.delete_document(
        session=db_session,
        document_id=decoded_document_id
    )
    logger.info(
        "deleted document",
        project_id=str(decoded_project_id),
        document_id=str(decoded_document_id)
    )