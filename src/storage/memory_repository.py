from datetime import datetime

from memory.models import Memory
from .json_repository import JsonRepository


class MemoryRepository:
    def __init__(self, repository: JsonRepository):
        self.repository = repository

    def save_all(self, memories: list[Memory]) -> None:
        data = [
            {
                "content": memory.content,
                "created_at": memory.created_at.isoformat(),
            }
            for memory in memories
        ]

        self.repository.save(data)

    def load_all(self) -> list[Memory]:
        data = self.repository.load()

        if data is None:
            return []

        return [
            Memory(
                content=item["content"],
                created_at=datetime.fromisoformat(item["created_at"]),
            )
            for item in data
        ] 
