import datetime
import dataclasses
from uuid import UUID


@dataclasses.dataclass
class Project:
    uuid: UUID
    title: str
    description: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None