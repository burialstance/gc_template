from dataclasses import dataclass

from dishka import FromDishka as Depends
from dishka.integrations.litestar import inject
from litestar import Controller, get

from app.infrastructure.sqla.database import Database
from app.infrastructure.background.broker import broker


@dataclass(kw_only=True)
class DatabaseHealthcheck:
    ok: bool


@dataclass(kw_only=True)
class HealthcheckResponse:
    database: DatabaseHealthcheck


class HealthcheckController(Controller):
    path = '/healthcheck'
    tags = ['healthcheck']

    @get()
    @inject
    async def healthcheck(
            self,
            database: Depends[Database]
    ) -> HealthcheckResponse:
        is_database_available = await database.ping()

        return HealthcheckResponse(
            database=DatabaseHealthcheck(ok=is_database_available),

        )
