import time
from dataclasses import dataclass

from litestar.datastructures import MutableScopeHeaders
from litestar.middleware import MiddlewareProtocol
from litestar.types import ASGIApp, Scope, Receive, Send, Message

@dataclass
class XProcessTimeHeader(MiddlewareProtocol):
    app: ASGIApp

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] == "http":
            start_time = time.time()

            async def send_wrapper(message: Message) -> None:
                if message["type"] == "http.response.start":
                    process_time = time.time() - start_time
                    headers = MutableScopeHeaders.from_message(message=message)
                    headers["X-Process-Time"] = str(round(process_time, 5))
                await send(message)

            await self.app(scope, receive, send_wrapper)
        else:
            await self.app(scope, receive, send)