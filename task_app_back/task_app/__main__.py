import uvicorn
from os import environ
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from . import task


app = FastAPI()

app.include_router(task.app)

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
