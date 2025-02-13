from .schema import Project
from .utils import query_execute


__all__ = [
    'projects',
    'create',
    'update',
    'delete'
]


def projects() -> None:
    pass


def create(project: Project) -> None:
    pass


def update(project: Project) -> None:
    pass


def delete(project_id: str) -> None:
    pass