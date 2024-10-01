from fastapi import FastAPI
import uvicorn
from . import task
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(task.app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
