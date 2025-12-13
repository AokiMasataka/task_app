import psycopg2.extras
import uvicorn
from os import environ
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from .api import task, project, doc


psycopg2.extras.register_uuid()
app = FastAPI()

parent = APIRouter()
parent.include_router(project.router)
parent.include_router(task.router)
parent.include_router(doc.router)

app.include_router(parent, prefix="/api")

# app.include_router(project.router)
# app.include_router(task.router)
# app.include_router(doc.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

host = environ.get(key="HOST", default="0.0.0.0")
port = int(environ.get(key="PORT", default="8000"))

if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port, log_level="debug")
