from dishka import Provider, provide, Scope

from app.main.config import SQLASettings


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def sqla_settings(self) -> SQLASettings:
        return SQLASettings.from_env()
