from bazario.asyncio import Dispatcher, Registry
from bazario.asyncio.resolvers.dishka import DishkaResolver
from dishka import Provider, provide, Scope, WithParents, AsyncContainer




class BazarioRegistryProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_resolver(self, container: AsyncContainer) -> DishkaResolver:
        return DishkaResolver(container=container)

    @provide(scope=Scope.REQUEST)
    def dispatcher(self, resolver: DishkaResolver, registry: Registry) -> WithParents[Dispatcher]:
        return Dispatcher(resolver=resolver, registry=registry)

    @provide(scope=Scope.APP)
    def provide_registry(self) -> Registry:
        _registry = Registry()

        return _registry
