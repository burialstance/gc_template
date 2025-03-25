from contextlib import AbstractAsyncContextManager
from typing import Callable, Sequence

from litestar import Litestar, Request, Response, MediaType, status_codes, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin, ScalarRenderPlugin

from .controllers import root_router
from .deps import create_collection_dependencies
from .middlewares.process_time_header import XProcessTimeHeader




def create_litestar_app(
        debug: bool,
        lifespan: Sequence[Callable[[Litestar], AbstractAsyncContextManager] | AbstractAsyncContextManager]
) -> Litestar:
    return Litestar(
        debug=debug,
        route_handlers=[root_router],
        middleware=[XProcessTimeHeader],
        dependencies=create_collection_dependencies(),
        lifespan=lifespan,
        openapi_config=OpenAPIConfig(
            title='OpenAPI',
            version='0.0.1',
            render_plugins=[ScalarRenderPlugin()]
        ),
    )
