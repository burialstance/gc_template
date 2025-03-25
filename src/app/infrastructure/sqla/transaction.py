from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.common.transaction import Transaction


class SQLATransaction(Transaction):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        try:
            await self._session.commit()
        except IntegrityError:
            await self.rollback()
            raise

    async def rollback(self) -> None:
        await self._session.rollback()
