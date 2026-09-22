from .models import ContextItem
from .provider import ContextProvider


class StaticContextProvider(ContextProvider):
    """Provides a predefined set of context items."""

    def __init__(self, items: list[ContextItem]):
        self._items = list(items)

    def provide(self) -> list[ContextItem]:
        return list(self._items)
