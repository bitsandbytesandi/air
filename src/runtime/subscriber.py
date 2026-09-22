from abc import ABC, abstractmethod

from .events import RuntimeEvent


class RuntimeEventSubscriber(ABC):
    """Defines the contract for runtime event consumers."""

    @abstractmethod
    def handle(self, event: RuntimeEvent) -> None:
        """Handle one runtime event."""
        raise NotImplementedError
