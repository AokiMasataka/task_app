import time
import httpx
from jose import jwt
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

from core import config, get_logger

logger = get_logger(__name__)


def fetch_jwk() -> str:
    url = f"{config.user_auth_service_url}/jwk"
    for _ in range(3):
        response  = httpx.get(url=url)
        if response.status_code == 200:
            break
        logger.warning("Failed to fetch JWK, retrying...")
        time.sleep(3)

    response_body = response.json()
    jwk = response_body["jwk"]

    logger.info("Fetched JWK successfully")
    return jwk


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

        token = auth.split(" ", 1)[1]

        try:
            jwk = request.app.state.jwk
            payload = jwt.decode(
                token,
                jwk,
                algorithms=["RS256"],
            )

            request.state.user_id = payload["id"]

        except Exception:
            return JSONResponse(status_code=401, content={"detail": "Invalid token"})

        return await call_next(request)