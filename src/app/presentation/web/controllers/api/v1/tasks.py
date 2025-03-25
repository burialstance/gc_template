from typing import Optional

from dishka import FromDishka as Depends
from dishka.integrations.litestar import inject

from litestar import Controller, post, get
from litestar.di import Provide
from litestar.params import Parameter, Dependency
from litestar.exceptions import NotFoundException
from taskiq import TaskiqResult, AsyncBroker
from taskiq.depends.progress_tracker import TaskProgress

from app.infrastructure.background.broker import broker as background_broker
from app.infrastructure.background.tasks.test import test_task

class TaskController(Controller):
    path = '/tasks'
    tags = ['tasks']

    dependencies = {
        'broker': Provide(lambda: background_broker, use_cache=True, sync_to_thread=True)
    }

    @post()
    async def create_task(
            self,
            value: int = Parameter(default=20),
    ) -> str:
        task = await test_task.kiq(value=value)
        return task.task_id

    @get('/{task_id:str}')
    async def get_result(
            self,
            task_id: str,
            broker: AsyncBroker = Dependency()
    ) -> TaskiqResult[int]:
        if not await broker.result_backend.is_result_ready(task_id):
            if not await broker.result_backend.get_progress(task_id):
                raise NotFoundException(detail='task with id={} not found'.format(task_id))
            raise NotFoundException(detail='task with id={} is not ready yet'.format(task_id))

        return await broker.result_backend.get_result(task_id, with_logs=True)



    @get('/{task_id:str}/progress')
    async def get_progress(
            self,
            task_id: str,
            broker: AsyncBroker = Dependency()
    ) -> TaskProgress[int]:
        progress: Optional[TaskProgress] = await broker.result_backend.get_progress(task_id)
        if progress is None:
            raise NotFoundException(detail='task with id={} not found'.format(task_id))

        return await broker.result_backend.get_progress(task_id)

