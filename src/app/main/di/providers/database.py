from typing import AsyncIterable

from dishka import Provider, provide, Scope
from sqlalchemy.ext.asyncio import AsyncSession

from app.main.config import SQLASettings
from app.application.common.transaction import Transaction
from app.infrastructure.sqla.transaction import SQLATransaction
from app.infrastructure.sqla.database import Database


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def database(self, settings: SQLASettings) -> Database:
        return Database(
            url=settings.url,
            echo=settings.echo
        )

    @provide(scope=Scope.REQUEST)
    async def session(self, database: Database) -> AsyncIterable[AsyncSession]:
        async with database.session() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    def transaction(self, session: AsyncSession) -> Transaction:
        return SQLATransaction(session=session)
