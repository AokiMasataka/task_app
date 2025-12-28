from uuid import UUID, uuid4
from typing import Literal

from sqlalchemy import desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Document


async def list_documents(
    session: AsyncSession,
    project_id: UUID,
    offset: int,
    limit: int,
    sort_by: Literal["created_at", "updated_at"] = "updated_at",
    sort_order: Literal["asc", "desc"] = "desc"
) -> tuple[list[Document], int]:
    stmt = select(Document).where(Document.project_id == project_id)

    sort_column = Document.updated_at if sort_by == "updated_at" else Document.created_at
    if sort_order == "desc":
        stmt = stmt.order_by(desc(sort_column))
    else:
        stmt = stmt.order_by(sort_column)
    
    # Get total count
    count_stmt = select(func.count()).select_from(Document).where(Document.project_id == project_id)
    result = await session.execute(count_stmt)
    total = result.scalar_one()
    
    stmt = stmt.offset(offset).limit(limit)

    # Execute query
    result = await session.execute(stmt)
    documents = result.scalars().all()

    return documents, total


async def get_document_by_id(
    session: AsyncSession,
    document_id: UUID
) -> Document | None:
    stmt = select(Document).where(Document.id == document_id)
    result = await session.execute(stmt)
    document = result.scalar_one_or_none()
    return document


async def create_document(
    session: AsyncSession,
    project_id: UUID,
    title: str,
    content: str
) -> UUID:
    uid = uuid4()
    document = Document(
        id=uid,
        project_id=project_id,
        title=title,
        content=content
    )
    session.add(document)
    await session.commit()
    return uid


async def update_document(
    session: AsyncSession,
    document_id: UUID,
    title: str | None = None,
    content: str | None = None
) -> Document:
    document = await session.get(Document, document_id)
    if not document:
        raise ValueError("Document not found.")
    
    if title is not None:
        document.title = title
    if content is not None:
        document.content = content
    
    session.add(document)
    await session.commit()
    await session.refresh(document)
    return document


async def delete_document(session: AsyncSession, document_id: UUID) -> None:
    document = await session.get(Document, document_id)
    if not document:
        raise ValueError("Document not found.")
    
    await session.delete(document)
    await session.commit()