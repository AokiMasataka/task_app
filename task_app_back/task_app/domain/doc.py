from typing import List
from uuid import UUID
from ..schemas import Doc
from ..service import doc as doc_service


def get_all(project_id: UUID) -> List[Doc]:
    docs = doc_service.get_all(project_id=project_id)
    docs = [Doc(**doc, project_id=project_id) for doc in docs]
    return docs


def get(project_id: UUID, doc_id: UUID) -> Doc:
    doc = doc_service.get(project_id=project_id, doc_id=doc_id)
    doc = Doc(**doc, project_id=project_id)
    return doc


def create(project_id: UUID, title: str, content: str) -> UUID:
    new_doc = Doc.new(project_id=project_id, title=title, content=content)
    doc_service.create(doc=new_doc)
    return new_doc.id


def update(
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
    doc_service.update(doc=update_doc)
    return update_doc


def delete(prproject_id: UUID, doc_id: UUID) -> None:
    doc_service.delete(project_id=prproject_id, doc_id=doc_id)