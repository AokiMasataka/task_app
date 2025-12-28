from uuid import UUID
from typing import Literal

from sqlalchemy.ext.asyncio import AsyncSession

from infra import Document, document_repository
from .exceptions import DocumentNotFoundError
from .project_service import _valiedate_clamps



async def list_documents(
    session: AsyncSession,
    project_id: UUID,
    page: int = 1,
    per_page: int = 10,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Document], int]:
    
    if _valiedate_clamps(value=page, min_value=1) is False:
        raise ValueError("Page must be greater than 0.")
    
    if _valiedate_clamps(value=per_page, min_value=1, max_value=100) is False:
        raise ValueError("Limit must be between 1 and 100.")
    
    offset = (page - 1) * per_page

    return await document_repository.list_documents(
        session=session,
        project_id=project_id,
        offset=offset,
        limit=per_page,
        sort_by=sort_by,
        sort_order=sort_order
)


async def get_document(
    session: AsyncSession,
    document_id: UUID
) -> Document:
    document = await document_repository.get_document_by_id(
        session=session,
        document_id=document_id
    )
    if document is None:
        raise DocumentNotFoundError("Document not found.")
    return document


async def create_document(
    session: AsyncSession,
    project_id: UUID,
    title: str,
    content: str
) -> UUID:
    return await document_repository.create_document(
        session=session,
        project_id=project_id,
        title=title,
        content=content
    )


async def update_document(
    session: AsyncSession,
    document_id: UUID,
    title: str | None = None,
    content: str | None = None
) -> Document:
    try:
        updated_document = await document_repository.update_document(
            session=session,
            document_id=document_id,
            title=title,
            content=content
        )
    except ValueError:
        raise DocumentNotFoundError("Document not found.")

    return updated_document


async def delete_document(
    session: AsyncSession,
    document_id: UUID
) -> None:
    await document_repository.delete_document(
        session=session,
        document_id=document_id
    )