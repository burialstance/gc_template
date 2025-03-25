from taskiq_redis import RedisStreamBroker, RedisAsyncResultBackend, ListQueueBroker

from app.main.config import TaskiqSettings

settings = TaskiqSettings.from_env()  # TODO: YOU RECEIVE NEW ACHIEVEMENT: "GLOBAL! AHTUNG" +50exp

broker = RedisStreamBroker(
    settings.broker_url
).with_result_backend(
    RedisAsyncResultBackend(
        settings.result_backend_url
    )
)

