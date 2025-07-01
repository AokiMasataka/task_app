from typing import List
from uuid import UUID
from ..schemas import Project
from ..service import project


async def create(title: str, description: str) -> UUID:
    new_project = Project.new(title=title, description=description)
    
    return (await project.create(new_project)).id


async def get_all() -> List[Project]:
    dict_projects = await project.get_all()
    projects = [
        Project(
            id=dict_project["id"],
            title=dict_project["title"],
            description=dict_project["description"],
            created_at=dict_project["created_at"],
            updated_at=dict_project["updated_at"]
        ) for dict_project in dict_projects]
    return projects


async def get(project_id: UUID) -> Project:
    dict_project = await project.get(project_id=project_id)
    return Project(
        id=dict_project["id"],
        title=dict_project["title"],
        description=dict_project["description"],
        created_at=dict_project["created_at"],
        updated_at=dict_project["updated_at"]
    )


async def update(project_id: UUID, title: str, description: str) -> Project:
    updated_project = Project.new_update(
        id=project_id,
        title=title,
        description=description
    )
    await project.update(project=updated_project)
    return updated_project


async def delete(project_id: UUID) -> None:
    await project.delete(project_id=project_id)
