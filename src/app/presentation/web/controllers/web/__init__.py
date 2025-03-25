from litestar import Router

from .index import IndexPageController

router = Router(
    path='/',
    route_handlers=[
        IndexPageController
    ]
)