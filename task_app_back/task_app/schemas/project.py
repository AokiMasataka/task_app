import datetime
import dataclasses
from uuid import UUID, uuid4


@dataclasses.dataclass
class Project:
    id: UUID
    title: str
    description: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    @staticmethod
    def new(title: str, description: str) -> "Project":
        project = Project(
            id=uuid4(),
            title=title,
            description=description,
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )
        return project

    @staticmethod
    def new_update(id: UUID, title: str, description: str) -> "Project":
        project = Project(
            id=id,
            title=title,
            description=description,
            created_at=None,
            updated_at=datetime.datetime.now()
        )
        return project