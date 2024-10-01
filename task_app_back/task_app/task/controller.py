from logging import getLogger
import uuid
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from . import task


logger = getLogger("uvicorn.app")
app = APIRouter()


class CreateRequest(BaseModel):
    title: str
    content: str


@app.post("/task", status_code=201)
def create_task(create_request: CreateRequest):
    task_id = str(uuid.uuid4())
    task.create(
        task_id=task_id,
        title=create_request.title,
        content=create_request.content
    )
    logger.info(msg=f"task created! task_ID: {task_id}")
    return JSONResponse(content={"task_id": task_id})


@app.get("/task", status_code=200)
def get_all():
    tasks = [task.json(inclede_content=False) for task in task.get_all()]
    logger.info(msg=f"get all tasks: number of tasks: {len(tasks)}")
    return {"tasks": tasks}


@app.get("/task/{task_id}", status_code=200)
def get_task(task_id):
    t = task.get(task_id=task_id)
    logger.info(msg=f"get task: task_ID: {task_id} title: {t.title}")
    return t.json()


@app.put("/task/{task_id}", status_code=200)
def update_task(task_id, create_request: CreateRequest):
    task.update(
        task_id=task_id,
        title=create_request.title,
        content=create_request.content
    )


@app.delete("/task/{task_id}", status_code=200)
def delete_task(task_id):
    task.delete(task_id=task_id)
    logger.info(msg=f"task deleted! task_ID: {task_id}")
