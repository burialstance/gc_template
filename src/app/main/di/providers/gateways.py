from dishka import Provider, Scope, provide


class GatewayProvider(Provider):
    scope = Scope.REQUEST
