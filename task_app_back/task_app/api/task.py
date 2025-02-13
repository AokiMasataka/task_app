from typing import Union
import datetime
from logging import getLogger
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from ..model import Task, task


logger = getLogger("uvicorn.app")
app = APIRouter()


class CreateRequest(BaseModel):
    title: str
    content: str
    status: int
    priority: int
    duedate: Union[str, None] = None


class GetTasksRequest(BaseModel):
    status: int


@app.post("/task", status_code=201)
def create_task(create_request: CreateRequest):
    print(create_request)
    if create_request.title == "":
        return JSONResponse(content={"message": "task title is required"}, status_code=400)

    if create_request.duedate is not None:
        duedate = datetime.datetime.strptime(create_request.duedate, "%Y-%m-%d").date()
    else:
        duedate = create_request.duedate
    new_task = Task(
        title=create_request.title,
        content=create_request.content,
        status=create_request.status,
        priority=create_request.priority,
        duedate=duedate
    )

    task.create(task=new_task)

    task_id = str(new_task.uuid)
    logger.info(msg=f"task created! task_ID: {task_id}")
    return JSONResponse(content={"task_id": task_id})


@app.get("/task", status_code=200)
def get_tasks(status: int = 0):
    tasks = task.get_tasks_with_status(
        status=status
    )
    logger.info(msg=f"get all tasks: number of tasks: {len(tasks)}")
    return {"tasks": tasks}


@app.get("/task/{task_id}", status_code=200)
def get_task(task_id):
    t = task.get(task_id=task_id)
    logger.info(msg=f"get task: task_ID: {task_id} title: {t['title']}")
    return t


@app.put("/task/{task_id}", status_code=200)
def update_task(task_id, create_request: CreateRequest):
    if create_request.duedate is not None:
        duedate = datetime.datetime.strptime(create_request.duedate, "%Y-%m-%d").date()
    else:
        duedate = create_request.duedate
    
    updated_task = Task(
        uuid=task_id,
        title=create_request.title,
        content=create_request.content,
        status=create_request.status,
        priority=create_request.priority,
        duedate=duedate
    )

    task.update(task=updated_task)
    logger.info(msg=f"update task: task_ID: {task_id} title: {updated_task.title}")


@app.delete("/task/{task_id}", status_code=200)
def delete_task(task_id):
    task.delete(task_id=task_id)
    logger.info(msg=f"task deleted! task_ID: {task_id}")
