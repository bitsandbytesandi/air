from .event_dispatcher import RuntimeEventDispatcher
from .event_factory import RuntimeEventFactory
from .event_publisher import RuntimeEventPublisher
from .event_stream import RuntimeEventStream
from .stream_service import RuntimeStreamService
from .subscriber_registry import RuntimeSubscriberRegistry


class RuntimeSystem:
    """Composes the runtime streaming subsystem."""

    def __init__(
        self,
        event_factory: RuntimeEventFactory,
        stream: RuntimeEventStream,
        service: RuntimeStreamService,
        registry: RuntimeSubscriberRegistry,
    ):
        self.event_factory = event_factory
        self.stream = stream
        self.service = service
        self.registry = registry


def create_runtime_system() -> RuntimeSystem:
    """Create the default runtime streaming subsystem."""

    stream = RuntimeEventStream()
    publisher = RuntimeEventPublisher(stream)

    registry = RuntimeSubscriberRegistry()
    dispatcher = RuntimeEventDispatcher(registry)

    service = RuntimeStreamService(
        publisher=publisher,
        dispatcher=dispatcher,
    )

    event_factory = RuntimeEventFactory()

    return RuntimeSystem(
        event_factory=event_factory,
        stream=stream,
        service=service,
        registry=registry,
    )
