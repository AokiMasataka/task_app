from typing import List
from uuid import UUID
from ..schemas import Doc
from ..service import doc as doc_service



async def get_all(project_id: UUID) -> List[Doc]:
    docs = await doc_service.get_all(project_id=project_id)
    docs = [Doc(**doc, project_id=project_id) for doc in docs]
    return docs


async def get(doc_id: UUID) -> Doc:
    doc = await doc_service.get(doc_id=doc_id)
    doc = Doc(**doc)
    return doc


async def create(project_id: UUID, title: str, content: str) -> UUID:
    new_doc = await Doc.new(project_id=project_id, title=title, content=content)
    doc_service.create(doc=new_doc)
    return new_doc.id


async def update(
    doc_id: UUID,
    project_id: UUID,
    title: str,
    content: str
) -> Doc:
    update_doc = Doc(
        id=doc_id,
        project_id=project_id,
        title=title,
        content=content
    )
    await doc_service.update(doc=update_doc)
    return update_doc


async def delete(doc_id: UUID) -> None:
    await doc_service.delete(doc_id=doc_id)