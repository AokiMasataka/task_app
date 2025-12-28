from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from core import config, get_logger
from .models import Base


logger = get_logger()

# Create async engine using config
DATABASE_URL = f"postgresql+asyncpg://{config.postgres_user}:{config.postgres_password}@{config.postgres_host}:{config.postgres_port}/{config.postgres_db}"

_engine = create_async_engine(
    DATABASE_URL,
    poolclass=NullPool,
    echo=False,
)

# Create async session factory
async_session_maker = sessionmaker(_engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with _engine.begin() as conn:
        await conn.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized")

async def close_db() -> None:
    global _engine
    if _engine:
        await _engine.dispose()
        _engine = None


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
