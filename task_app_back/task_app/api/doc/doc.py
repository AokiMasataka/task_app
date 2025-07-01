from logging import getLogger
from uuid import UUID
from fastapi import APIRouter
from .doc_schema import (
    DocCreateRequest,
    DocCreateResponse,
    DocGetResponse,
    DocGetAllResponse,
    DocUpdateRequest,
    DocUpdateResponse
)

from ... import domain


logger = getLogger("uvicorn.app")
router = APIRouter()


@router.get(
    "/projects/{project_id}/docs/{doc_id}",
    status_code=200,
    response_model=DocGetResponse
)
async def get_doc(project_id: UUID, doc_id: UUID):
    doc = await domain.doc.get(doc_id=doc_id)
    return DocGetResponse(
        id=doc.id,
        project_id=doc.project_id,
        title=doc.title,
        content=doc.content
    )


@router.get(
    "/projects/{project_id}/docs/",
    status_code=200,
    response_model=DocGetAllResponse
)
async def get_docs(project_id: UUID):
    docs = await domain.doc.get_all(project_id=project_id)
    docs = [
        DocGetResponse(
            id=doc.id,
            project_id=doc.project_id,
            title=doc.title,
            content=doc.content
        ) for doc in docs
    ]
    return DocGetAllResponse(results=docs, count=len(docs), next=None, prev=None)


@router.post(
    "/projects/{project_id}/docs/",
    status_code=201,
    response_model=DocCreateResponse
)
async def cretae_doc(project_id: UUID, create_request: DocCreateRequest):
    doc_id = await domain.doc.create(
        project_id=project_id,
        title=create_request.title,
        content=create_request.content
    )
    return DocCreateResponse(id=doc_id)


@router.put(
    "/projects/{project_id}/docs/{doc_id}",
    status_code=200,
    response_model=DocUpdateResponse
)
async def update_doc(project_id: UUID, doc_id:  UUID, update_request: DocUpdateRequest):
    updated_doc = await domain.doc.update(
        doc_id=doc_id,
        project_id=project_id,
        title=update_request.title,
        content=update_request.content
    )

    return DocUpdateResponse(
        id=updated_doc.id,
        project_id=updated_doc.project_id,
        title=updated_doc.title,
        content=updated_doc.content
    )


@router.delete("/projects/{project_id}/docs/{doc_id}", status_code=204)
async def delete_doc(project_id: UUID, doc_id: UUID):
    await domain.doc.delete(doc_id=doc_id)