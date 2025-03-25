import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime

from src.application.common.timezone import now


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: now()
    )
    updated_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True),
        default=None,
        onupdate=lambda: now()
    )
