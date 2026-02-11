import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# from routings import build_api_router
from routings.apis import router
from middlewares import fetch_jwk
from core import get_logger, config


logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    limits = httpx.Limits(
        max_connections=1000,
        max_keepalive_connections=200
    )

    timeout = httpx.Timeout(
        connect=2.0,
        read=5.0,
        write=5.0,
        pool=1.0,
    )

    app.state.http_client = httpx.AsyncClient(
        limits=limits,
        timeout=timeout,
        # http2=True,   # 可能なら必須
    )

    # app.state.jwk = fetch_jwk()

    yield

    await app.state.http_client.aclose()


app = FastAPI(title="task_app_gateway", lifespan=lifespan)

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


app.include_router(router=router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=config.app_port,
        log_level="debug",
        # access_log=False
    )
