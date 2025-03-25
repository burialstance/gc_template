from contextlib import asynccontextmanager

from dishka.integrations.litestar import setup_dishka as setup_dishka_litestar
from litestar import Litestar

from app.infrastructure.background.broker import broker
from app.infrastructure.background.lifespan import AsyncBrokerLifespan
from app.infrastructure.sqla.database import Database
from app.presentation.web.app import create_litestar_app
from app.main.di.container import async_container

import logging

logging.basicConfig(level=logging.DEBUG)


@asynccontextmanager
async def broker_lifespan(app: Litestar):
    async with AsyncBrokerLifespan(broker):
        yield


async def on_startup(app: Litestar):
    app.get_logger().info('on_startup')
    async with app.state.dishka_container() as ioc:
        db: Database = await ioc.get(Database)
        await db.create_tables()


async def on_shutdown(app: Litestar):
    app.get_logger().info('on_shutdown')
    await app.state.dishka_container.close()


def create_app() -> Litestar:
    _app = create_litestar_app(
        debug=True,
        lifespan=[]
    )
    setup_dishka_litestar(async_container, _app)

    _app.on_startup.append(on_startup)
    _app.on_shutdown.append(on_shutdown)

    return _app


app = create_app()
