from litestar.di import Provide

from . import pagination

def create_collection_dependencies() -> dict[str, Provide]:
    return {
        'pagination': Provide(pagination.provide_limit_offset_pagination, sync_to_thread=False),
    }