from contextlib import asynccontextmanager
from typing import AsyncIterable

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.infrastructure.sqla.models.base import Model


class Database:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            future=True,
            poolclass=NullPool
        )
        self.async_session_factory = async_sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
        )

    @asynccontextmanager
    async def session(self) -> AsyncIterable[AsyncSession]:
        async with self.async_session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)

    async def ping(self) -> bool:
        async with self.engine.connect():
            return True
