from datetime import datetime

from .models import Memory
from .store import MemoryStore
from storage.memory_repository import MemoryRepository


class MemoryService:
    def __init__(
        self,
        store: MemoryStore,
        repository: MemoryRepository,
    ):
        self.store = store
        self.repository = repository

    def remember(
        self,
        content: str,
    ) -> Memory:
        memory = Memory(
            content=content,
            created_at=datetime.now(),
        )

        self.store.add(memory)
        self.repository.save_all(
            self.store.all()
        )

        return memory

    def restore(self) -> None:
        memories = self.repository.load_all()

        self.store.replace_all(
            memories
        )

    def get_all(self) -> list[Memory]:
        return self.store.all()

    def search(
        self,
        query: str,
    ) -> list[Memory]:
        normalized_query = query.strip().casefold()

        if not normalized_query:
            return self.get_all()

        return [
            memory
            for memory in self.store.all()
            if normalized_query
            in memory.content.casefold()
        ]
