from .bus import EventBus
from .models import ApplicationEvent


class EventPublisher:
    def __init__(
        self,
        bus: EventBus,
    ):
        self.bus = bus

    def publish(
        self,
        event: ApplicationEvent,
    ) -> None:
        self.bus.publish(event)
