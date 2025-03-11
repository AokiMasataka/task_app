from typing import List
from uuid import UUID
from ..schemas import Project
from ..service import project



def create(title: str, description: str) -> UUID:
    new_project = Project.new(title=title, description=description)
    project.create(new_project)
    return new_project.uuid


def get_all() -> List[Project]:
    dict_projects = project.get_all()
    projects = [
        Project(
            uuid=dict_project["id"],
            title=dict_project["title"],
            description=dict_project["description"],
            created_at=dict_project["created_at"],
            updated_at=dict_project["updated_at"]
        ) for dict_project in dict_projects]
    return projects


def get(project_id: UUID) -> Project:
    dict_project = project.get(project_id=project_id)
    return Project(
        uuid=dict_project["id"],
        title=dict_project["title"],
        description=dict_project["description"],
        created_at=dict_project["created_at"],
        updated_at=dict_project["updated_at"]
    )


def update(project_id: UUID, title: str, description: str) -> None:
    updated_project = Project.new_update(
        project_id=project_id,
        title=title,
        description=description
    )
    project.update(project=updated_project)


def delete(project_id: UUID) -> None:
    project.delete(project_id=project_id)
