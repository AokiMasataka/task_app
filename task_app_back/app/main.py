from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from apis import project_router, task_router, document_router
from infra import init_db, close_db
from core import get_logger, config


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    try:
        await init_db()
        logger.info("Database initialized successfully.")
        yield
    finally:
        await close_db()


app = FastAPI(title="task-app-back", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)
    if request.method != "OPTIONS":
        logger.info(
            "request.completed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code
        )
    return response


app.include_router(project_router)
app.include_router(task_router)
app.include_router(document_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=config.app_port,
        access_log=False
    )
