from abc import ABC, abstractmethod

from .models import ContextItem


class ContextProvider(ABC):
    """Defines the contract for a source of context items."""

    @abstractmethod
    def provide(self) -> list[ContextItem]:
        """Return context items supplied by this provider."""
        raise NotImplementedError
