from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource

from app.infrastructure.background.broker import broker

scheduler = TaskiqScheduler(
    broker,
    [LabelScheduleSource(broker)],
)
