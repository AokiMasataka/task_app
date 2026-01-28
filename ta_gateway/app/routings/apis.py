import httpx
from fastapi import APIRouter, Request, Response, HTTPException, Depends
from fastapi.responses import StreamingResponse

from .deps import get_http_client
from core import config, get_logger

logger = get_logger(__name__)


SERVICE_ROUTES = {
        "projects": config.project_service_url,
        "login": config.user_auth_service_url,
        "register": config.user_auth_service_url,
        "users": config.user_auth_service_url,
}


def _resolve_backend_path(path: str) -> str:
    splited_path = path.split("/")
    first = splited_path[0]

    
    if first not in SERVICE_ROUTES:
        raise HTTPException(status_code=404, detail="service not found")
    
    backend = SERVICE_ROUTES[first]

    return backend + "/" + path


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
    
    logger.info("requested", user_id="aaaa")
    
    url = _resolve_backend_path(path=full_path)

    body = await request.body()

    HOP_HEADERS = {
        "host",
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "transfer-encoding",
        "upgrade",
        "content-length",
    }

    forward_headers = {
        k: v
        for k, v in request.headers.items()
        if k.lower() not in HOP_HEADERS
    }
            
    response = await http_client.request(
        method=request.method,
        url=url,
        headers=forward_headers,
        params=request.query_params,
        content=body,
    )


    HOP_HEADERS = {
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "transfer-encoding",
        "upgrade",
        "content-length",
    }

    filtered_headers = {
        k: v for k, v in response.headers.items()
        if k.lower() not in HOP_HEADERS
    }

    return Response(
        content=response.content,
        status_code=response.status_code,
        # headers=response.headers,
        # headers=filtered_headers,
    )


# def build_api_router() -> APIRouter:
#     router = APIRouter()
    
#     @router.api_route(
#         "/api/{full_path:path}",
#         methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"]
#     )
#     async def gateway(
#         full_path: str,
#         request: Request,
#         http_client: httpx.AsyncClient = Depends(get_http_client)
#     ) -> Response:
        
#         logger.info("requested", user_id="aaaa")
        
#         url = _resolve_backend_path(path=full_path)

#         body = await request.body()

#         HOP_HEADERS = {
#             "host",
#             "connection",
#             "keep-alive",
#             "proxy-authenticate",
#             "proxy-authorization",
#             "te",
#             "trailers",
#             "transfer-encoding",
#             "upgrade",
#             "content-length",
#         }

#         forward_headers = {
#             k: v
#             for k, v in request.headers.items()
#             if k.lower() not in HOP_HEADERS
#         }
                
#         response = await http_client.request(
#             method=request.method,
#             url=url,
#             headers=forward_headers,
#             params=request.query_params,
#             content=body,
#         )


#         HOP_HEADERS = {
#             "connection",
#             "keep-alive",
#             "proxy-authenticate",
#             "proxy-authorization",
#             "te",
#             "trailers",
#             "transfer-encoding",
#             "upgrade",
#             "content-length",
#         }

#         filtered_headers = {
#             k: v for k, v in response.headers.items()
#             if k.lower() not in HOP_HEADERS
#         }

#         return Response(
#             content=response.content,
#             status_code=response.status_code,
#             # headers=response.headers,
#             # headers=filtered_headers,
#         )

#     return router

