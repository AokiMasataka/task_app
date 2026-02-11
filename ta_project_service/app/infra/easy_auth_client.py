import uuid
import base64

from httpx import AsyncClient
from pydantic import BaseModel

from core import config, get_logger


logger = get_logger(__name__)


class User(BaseModel):
    id: uuid.UUID
    username: str
    email: str


async def get_users(
    client: AsyncClient,
) -> list[User]:
    headers = {
        "Content-Type": "application/json",
        "Authorization": _get_basic()
    }

    response = await client.get(
        url=config.ea_auth_url + "/api/users",
        headers=headers
    )

    try:
        response = response.json()
    except Exception as e:
        logger.error(
            "failed to parse response from Easy Auth",
            error=str(e),
            response_text=response.text,
            url=config.ea_auth_url + "/api/users"
        )
        raise RuntimeError("Failed to parse response from Easy Auth") from e

    users = response["users"]
    total = response["total"]

    for i in range(len(users)):
        users[i] = User(
            id=uuid.UUID(users[i]["id"]),
            username=users[i]["name"],
            email=users[i]["email"]
        )
    return users


async def get_user(
    client: AsyncClient,
    user_id: uuid.UUID
) -> User:
    headers = {
        "Content-Type": "application/json",
        "Authorization": _get_basic()
    }

    response = await client.get(
        url=f"{config.ea_auth_url}/api/users/{user_id}",
        headers=headers
    )

    user_data = response.json()
    return User(
        id=user_data["id"],
        username=user_data["name"],
        email=user_data["email"]
    )


async def create_user(
    client: AsyncClient,
    name: str,
    email: str,
    password: str
) -> uuid.UUID:
    headers = {
        "Content-Type": "application/json",
        "Authorization": _get_basic()
    }
    payload = {
        "name": name,
        "email": email,
        "pass": password
    }
    response = await client.post(
        url=config.ea_auth_url + "/api/users",
        headers=headers,
        json=payload
    )

    user_id = response.json()["id"]
    return uuid.UUID(user_id)

def _get_basic() -> str:
    data = config.client_id + ":" + config.client_secret
    encoded = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    return "Basic " + encoded