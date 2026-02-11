from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from .models import Base
from core import config, get_logger


logger = get_logger()


def create_db_engine() -> AsyncEngine:
    """Create database engine."""

    db_url = URL.create(
        drivername="postgresql+asyncpg",
        username=config.postgres_user,
        password=config.postgres_password,
        host=config.postgres_host,
        port=config.postgres_port,
        database=config.postgres_db,
    )
    return create_async_engine(url=db_url, echo=False)


def create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    """Create session maker."""
    return async_sessionmaker(engine, expire_on_commit=False)


async def init_db(engine: AsyncEngine) -> None:
    """Initialize database tables."""
    

    async with engine.begin() as conn:
        await conn.execute(text('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'))
        await conn.run_sync(Base.metadata.create_all)