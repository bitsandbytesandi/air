from .models import ApplicationEvent


class EventStore:
    def __init__(self):
        self._events: list[ApplicationEvent] = []

    def add(
        self,
        event: ApplicationEvent,
    ) -> None:
        self._events.append(event)

    def all(self) -> list[ApplicationEvent]:
        return list(self._events)

    def clear(self) -> None:
        self._events.clear()
