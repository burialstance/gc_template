from litestar import Router

from . import api
from . import web
from .healthcheck import HealthcheckController

root_router = Router(
    path='/',
    route_handlers=[
        HealthcheckController,
        web.router,
        api.router,
    ]
)