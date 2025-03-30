import datetime
import dataclasses
from uuid import UUID, uuid4


@dataclasses.dataclass
class Doc:
    id: UUID
    project_id: UUID
    title: str
    content: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()
        
        if self.updated_at is None:
            self.updated_at = datetime.datetime.now()
    
    @staticmethod
    def new(project_id: UUID, title: str, content: str | None = None) -> "Doc":
        return Doc(
            id=uuid4(),
            project_id=project_id,
            title=title,
            content=content
        )