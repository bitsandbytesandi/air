from .event_stream import RuntimeEventStream
from .events import RuntimeEvent


class RuntimeEventPublisher:
    """Publishes runtime events to an event stream."""

    def __init__(self, stream: RuntimeEventStream):
        self.stream = stream

    def publish(self, event: RuntimeEvent) -> None:
        self.stream.publish(event)
