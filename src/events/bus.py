from collections.abc import Callable
from typing import Protocol

from .models import ApplicationEvent


EventHandler = Callable[[ApplicationEvent], None]


class EventBus(Protocol):
    def publish(
        self,
        event: ApplicationEvent,
    ) -> None:
        ...

    def subscribe(
        self,
        handler: EventHandler,
    ) -> None:
        ...
