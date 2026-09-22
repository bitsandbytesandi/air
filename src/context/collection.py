from .models import ContextItem


class ContextCollection:
    """Stores context items for a single context assembly."""

    def __init__(self):
        self._items: list[ContextItem] = []

    def add(self, item: ContextItem) -> None:
        self._items.append(item)

    def get_all(self) -> list[ContextItem]:
        return list(self._items)
