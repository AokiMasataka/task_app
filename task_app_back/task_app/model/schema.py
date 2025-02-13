import datetime
from uuid import UUID, uuid4

import dataclasses

class Status:
    todo = 0
    doing = 1
    done = 2


@dataclasses.dataclass
class Task:
    title: str
    content: str
    uuid: None | UUID = None
    status: int = 0
    priority: int = 0
    duedate: datetime.date | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    def __post_init__(self):
        if self.uuid is None:
            self.uuid = uuid4()

        if self.created_at is None:
            self.created_at = datetime.datetime.now()
        
        if self.updated_at is None:
            self.updated_at = datetime.datetime.now()
