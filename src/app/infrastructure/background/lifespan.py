from taskiq import AsyncBroker


class AsyncBrokerLifespan:
    def __init__(self, broker: AsyncBroker):
        self.broker = broker

    async def __aenter__(self):
        if not self.broker.is_worker_process:
            await self.broker.startup()
            print('broker.startup')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self.broker.is_worker_process:
            await self.broker.shutdown()
            print('broker.shutdown')
