from .events import RuntimeEvent
from .subscriber import RuntimeEventSubscriber
from .subscriber_registry import RuntimeSubscriberRegistry


class RuntimeEventDispatcher:
    """Dispatches runtime events to registered subscribers."""

    def __init__(
        self,
        registry: RuntimeSubscriberRegistry,
    ):
        self.registry = registry

    def dispatch(self, event: RuntimeEvent) -> None:
        for subscriber in self.registry.get_all():
            subscriber.handle(event)
