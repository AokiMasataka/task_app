import datetime
from uuid import uuid4


class Status:
    todo = 0
    doing = 1
    done = 2


class Task:
    def __init__(
        self,
        title: str,
        content: str,
        uuid: str = None,
        status: int = Status.todo,
        created_at = None,
        updated_at = None
    ) -> None:
        self.title = title
        self.content = content
        self.status = status


        if uuid is None:
            self.uuid = uuid4()
        else:
            self.uuid = uuid

        if created_at is None:
            self.created_at = datetime.datetime.now()
        else:
            self.created_at = created_at
        
        if updated_at is None:
            self.updated_at = datetime.datetime.now()
        else:
            self.updated_at = updated_at
    
    def json(self, inclede_content: bool = True) -> dict:
        response = {
            "title": self.title,
            "id": str(self.uuid)
        }

        if inclede_content:
            response["content"] = self.content

        return response
    
    def from_json(item, uuid: str = None) -> "Task":
        return Task(title=item["title"], content=item["content"], uuid=uuid)