from .event_dispatcher import RuntimeEventDispatcher
from .event_publisher import RuntimeEventPublisher
from .events import RuntimeEvent


class RuntimeStreamService:
    """Application-facing service for runtime event streaming."""

    def __init__(
        self,
        publisher: RuntimeEventPublisher,
        dispatcher: RuntimeEventDispatcher,
    ):
        self.publisher = publisher
        self.dispatcher = dispatcher

    def publish(self, event: RuntimeEvent) -> None:
        self.publisher.publish(event)
        self.dispatcher.dispatch(event)
