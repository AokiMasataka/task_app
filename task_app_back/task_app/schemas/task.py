import datetime
import dataclasses
from uuid import UUID, uuid4


STATUS_TODO = 0
STATUS_DOING = 1
STATUS_DONE = 2

PRIORITY_LOW = 0
PRIORITY_MIDIAM = 1
PRIORITY_HIGH = 2


@dataclasses.dataclass
class Task:
    project_id: UUID
    title: str
    content: str
    uuid: UUID
    status: int = STATUS_TODO
    priority: int = PRIORITY_LOW
    duedate: datetime.date | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.datetime.now()
        
        if self.updated_at is None:
            self.updated_at = datetime.datetime.now()

    @staticmethod
    def new(
        project_id: UUID,
        title: str,
        content: str,
        status: int = STATUS_TODO,
        priority: int = PRIORITY_LOW,
        duedate: datetime.date | None = None
    ) -> "Task":
        return Task(
            uuid=uuid4(),
            project_id=project_id,
            title=title,
            content=content,
            status=status,
            priority=priority,
            duedate=duedate
        )