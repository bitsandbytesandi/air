from uuid import UUID

from .models import Memory


class MemoryStore:
    def __init__(self):
        self.memories: list[Memory] = []

    def add(
        self,
        memory: Memory,
    ) -> None:
        self.memories.append(memory)

    def replace_all(
        self,
        memories: list[Memory],
    ) -> None:
        self.memories = list(memories)

    def delete(
        self,
        memory_id: UUID,
    ) -> bool:
        for index, memory in enumerate(
            self.memories
        ):
            if memory.id == memory_id:
                del self.memories[index]
                return True

        return False

    def all(self) -> list[Memory]:
        return list(self.memories)
