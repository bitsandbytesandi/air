from .models import Memory

class MemoryStore:
    def __init__(self):
        self.memories: list[Memory] = []
    
    def add(self, memory: Memory) -> None:
        self.memories.append(memory)

    def all(self) -> list[Memory]:
        return list(self.memories)
