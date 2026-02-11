from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from apis import project_router, task_router, document_router, user_router
# from infra import init_db, close_db
from infra.database import create_db_engine, create_session_maker, init_db
from core import get_logger, config


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_db_engine()
    app.state.db_engine = engine
    app.state.db_session_maker = create_session_maker(engine)
    await init_db(engine)
    app.state.http_client = httpx.AsyncClient()
    yield
    await app.state.http_client.aclose()
    await app.state.db_engine.dispose()


app = FastAPI(title="task-app-back", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:80",
        "http://localhost:443",
        "http://localhost:3000"
    ],
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
app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=config.app_port,
        access_log=False
    )
