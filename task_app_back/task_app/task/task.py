import os
import json


TASK_DIR = "./tasks"


class Task:
    def __init__(self, title: str, content: str, uuid: str = None) -> None:
        self._title = title
        self._content = content
        self._uuid = uuid
    
    @property
    def title(self) -> str: 
        return self._title
    
    @property
    def content(self) -> str: 
        return self._content

    @property
    def id(self) -> str:
        return self._uuid
    
    def json(self, inclede_content: bool = True) -> dict:
        response = {
            "title": self._title,
            "id": self._uuid
        }

        if inclede_content:
            response["content"] = self._content

        return response
    
    def from_json(item, uuid: str = None) -> "Task":
        return Task(title=item["title"], content=item["content"], uuid=uuid)


def create(task_id: str, title: str, content: str) -> None:
    task_path = os.path.join(TASK_DIR, task_id)
    
    with open(file=task_path, mode="w") as f:
        json.dump(obj={"title": title, "content": content}, fp=f)


def get_all() -> list[Task]:
    task_ids = os.listdir(TASK_DIR)
    results = []
    for task_id in task_ids:
        task_path = os.path.join(TASK_DIR, task_id)
        with open(file=task_path, mode="r") as f:
            task_json = json.load(fp=f)
            results.append(Task.from_json(item=task_json, uuid=task_id))
    return results


def get(task_id: str) -> Task:
    task_path = os.path.join(TASK_DIR, task_id)

    with open(file=task_path, mode="r") as f:
        task = json.load(fp=f)
    return Task.from_json(item=task, uuid=task_id)


def update(task_id: str, title: str, content: str):
    create(task_id=task_id, title=title, content=content)


def delete(task_id: str) -> None:
    task_path = os.path.join(TASK_DIR, task_id)
    os.remove(task_path)
