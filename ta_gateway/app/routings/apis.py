import httpx
from fastapi import APIRouter, Request, Response, HTTPException, Depends
from fastapi.responses import StreamingResponse

from .deps import get_http_client
from core import config, get_logger

logger = get_logger(__name__)


SERVICE_ROUTES = {
    "authorize": config.user_auth_service_url,
    "token": config.user_auth_service_url,
    "refresh": config.user_auth_service_url,
    "logout": config.user_auth_service_url,
    "users": config.project_service_url,
    "projects": config.project_service_url,
}


def _resolve_backend_path(path: str) -> str:
    splited_path = path.split("/")
    first = splited_path[0]

    
    if first not in SERVICE_ROUTES:
        raise HTTPException(status_code=404, detail="service not found")
    
    backend = SERVICE_ROUTES[first]

    return backend + "/api/" + path


router = APIRouter()
    
@router.api_route(
    "/api/{full_path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]
)
async def gateway(
    full_path: str,
    request: Request,
    http_client: httpx.AsyncClient = Depends(get_http_client)
) -> Response:
    
    url = _resolve_backend_path(path=full_path)

    body = await request.body()

    logger.info(
        "proxy.request",
        method=request.method,
        path=full_path,
        url=url
    )

    response = await http_client.request(
        method=request.method,
        url=url,
        headers=request.headers,
        params=request.query_params,
        content=body,
    )

    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=response.headers,
    )
