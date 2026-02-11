from httpx import AsyncClient

from infra import easy_auth_client


async def fetch_all_users(client: AsyncClient) -> list[easy_auth_client.User]:
    return await easy_auth_client.get_users(client=client)


async def fetch_user(
    client: AsyncClient,
    user_id: str
) -> easy_auth_client.User:
    return await easy_auth_client.get_user(client=client, user_id=user_id)


async def create_user(
    client: AsyncClient,
    name: str,
    email: str,
    password: str
) -> str:
    user_id = await easy_auth_client.create_user(
        client=client,
        name=name,
        email=email,
        password=password
    )
    return user_id