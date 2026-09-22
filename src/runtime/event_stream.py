from .events import RuntimeEvent


class RuntimeEventStream:
    """Stores runtime events in publication order."""

    def __init__(self):
        self._events: list[RuntimeEvent] = []

    def publish(self, event: RuntimeEvent) -> None:
        self._events.append(event)

    def get_all(self) -> list[RuntimeEvent]:
        return list(self._events)
