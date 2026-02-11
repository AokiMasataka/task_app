from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends, Header, Request
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker



async def get_db_session(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with request.app.state.db_session_maker() as session:
        yield session


async def get_http_client(request: Request) -> AsyncClient:
    return request.app.state.http_client


DBSessionDep = Annotated[AsyncSession, Depends(get_db_session)]
HttpClientDep = Annotated[AsyncClient, Depends(get_http_client)]