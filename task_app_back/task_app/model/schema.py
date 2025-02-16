import datetime
import dataclasses
from uuid import UUID


STATUS_TODO = 0
STATUS_DOING = 1
STATUS_DONE = 2

PRIORITY_LOW = 0
PRIORITY_MIDIAM = 0
PRIORITY_HIGH = 0


@dataclasses.dataclass
class Task:
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
