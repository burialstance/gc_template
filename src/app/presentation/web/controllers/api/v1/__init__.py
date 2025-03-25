from litestar import Router

from . import tasks

router = Router(
    path='/v1',
    route_handlers=[
        tasks.TaskController
    ]
)
