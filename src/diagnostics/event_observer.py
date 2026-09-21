from events.models import ApplicationEvent
from .observability_service import ObservabilityService


class EventObserver:
    def __init__(self, observability: ObservabilityService):
        self.observability = observability

    def handle(self, event: ApplicationEvent) -> None:
        self.observability.record_observation(
            event.event_type.value,
            event.payload,
        )
