from collections.abc import Callable

from .models import ApplicationEvent
from .store import EventStore


EventHandler = Callable[[ApplicationEvent], None]


class ApplicationEventService:
    def __init__(
        self,
        store: EventStore,
    ):
        self.store = store
        self._handlers: list[EventHandler] = []

    def subscribe(
        self,
        handler: EventHandler,
    ) -> None:
        if handler in self._handlers:
            return

        self._handlers.append(handler)

    def publish(
        self,
        event: ApplicationEvent,
    ) -> None:
        self.store.add(event)

        for handler in self._handlers:
            handler(event)

    def events(self) -> list[ApplicationEvent]:
        return self.store.all()
