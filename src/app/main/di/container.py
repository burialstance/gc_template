from dishka.async_container import make_async_container

from .providers.config import ConfigProvider
from .providers.events import EventProvider
from .providers.gateways import GatewayProvider
from .providers.interactors import InteractorProvider
from .providers.registry import BazarioRegistryProvider
from .providers.database import DatabaseProvider

async_container = make_async_container(
    ConfigProvider(),
    GatewayProvider(),
    InteractorProvider(),
    BazarioRegistryProvider(),
    EventProvider(),
    DatabaseProvider(),
)
