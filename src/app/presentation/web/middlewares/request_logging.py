from litestar import Request
from litestar.middleware import MiddlewareProtocol
from litestar.types import Scope, Receive, Send


class MyRequestLoggingMiddleware(MiddlewareProtocol):
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            request = Request(scope)
            self.app.get_logger().info('{} {}'.format(request.method, request.url))
        await self.app(scope, receive, send)