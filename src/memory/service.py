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

    def remember(self, content: str) -> Memory:
        memory = Memory(
            content=content,
            created_at=datetime.now(),
        )

        self.store.add(memory)
        self.repository.save_all(self.store.all())

        return memory

    def restore(self) -> None:
        memories = self.repository.load_all()
        
        for memory in memories:
            self.store.add(memory)

    def get_all(self) -> list[Memory]:
        return self.store.all()
