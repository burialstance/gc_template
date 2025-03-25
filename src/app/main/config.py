import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

SRC_DIR = Path(__file__).parent.parent.parent


@dataclass
class SQLASettings:
    url: str
    echo: bool = False

    @classmethod
    def from_env(cls) -> 'SQLASettings':
        return cls(
            url=os.getenv('DATABASE_URL'),
            echo=os.getenv('DATABASE_ECHO', False),
        )


@dataclass
class TaskiqSettings:
    broker_url: str
    result_backend_url: Optional[str] = None

    def __post_init__(self):
        if self.result_backend_url is None:
            self.result_backend_url = self.broker_url

    @classmethod
    def from_env(cls) -> 'TaskiqSettings':
        return cls(
            broker_url=os.getenv('TASKIQ_BROKER_URL'),
            result_backend_url=os.getenv('TASKIQ_RESULT_BACKEND_URL')
        )

# @dataclass(kw_only=True)
# class TelegramBotSettings:
#     token: str
#     media_chat_id: int
#     webhook_url: Optional[str] = None
#     webhook_secret: str
#
#     @classmethod
#     def from_env(cls) -> 'TelegramBotSettings':
#         return cls(
#             token=os.getenv('TELEGRAM_BOT_TOKEN'),
#             webhook_url=os.getenv('TELEGRAM_BOT_WEBHOOK_URL'),
#             webhook_secret=os.getenv('TELEGRAM_BOT_WEBHOOK_SECRET', str(uuid4())),
#             media_chat_id=int(os.getenv('TELEGRAM_MEDIA_CHAT_ID')),
#         )
