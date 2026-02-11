import base64
from uuid import UUID
from typing import Literal

from fastapi import APIRouter

from core import get_logger
from services import user_service

from .schemas import UserResponse, UserCreateRequest
from ..deps import DBSessionDep, HttpClientDep

logger = get_logger(__name__)
user_router = APIRouter(tags=["users"], prefix="/api")


@user_router.get("/users")
async def list_users(
    client: HttpClientDep,
) -> list[UserResponse]:
    users = await user_service.fetch_all_users(
        client=client
    )

    logger.info("fetched all users", count=len(users))

    return [
        UserResponse(
            id=user.id,
            username=user.username,
            email=user.email
        )
        for user in users
    ]


@user_router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    client: HttpClientDep,
    user_id: str
) -> UserResponse:

    user = await user_service.fetch_user(
        client=client,
        user_id=user_id
    )

    logger.info(
        "fetched user",
        user_id=str(user_id)
    )

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email
    )


@user_router.post("/users", response_model=str)
async def create_user(
    client: HttpClientDep,
    request: UserCreateRequest
) -> str:

    user_id = await user_service.create_user(
        client=client,
        name=request.name,
        email=request.email,
        password=request.password
    )

    logger.info(
        "created user",
        user_id=str(user_id)
    )

    return {"user_id": str(user_id)}