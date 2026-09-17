from datetime import datetime
from uuid import UUID, uuid5

from memory.models import Memory
from .json_repository import JsonRepository


LEGACY_MEMORY_NAMESPACE = UUID(
    "4f6f5c6a-7f5c-4f7e-9d8c-7e7b5d2f1a10"
)


class MemoryRepository:
    def __init__(
        self,
        repository: JsonRepository,
    ):
        self.repository = repository

    def save_all(
        self,
        memories: list[Memory],
    ) -> None:
        data = [
            {
                "id": str(memory.id),
                "content": memory.content,
                "created_at": (
                    memory.created_at.isoformat()
                ),
            }
            for memory in memories
        ]

        self.repository.save(data)

    def load_all(self) -> list[Memory]:
        data = self.repository.load()

        if data is None:
            return []

        memories: list[Memory] = []

        for item in data:
            created_at = datetime.fromisoformat(
                item["created_at"]
            )

            memory_id = item.get("id")

            if memory_id:
                parsed_id = UUID(memory_id)
            else:
                parsed_id = uuid5(
                    LEGACY_MEMORY_NAMESPACE,
                    (
                        f"{item['content']}"
                        f"|{item['created_at']}"
                    ),
                )

            memories.append(
                Memory(
                    id=parsed_id,
                    content=item["content"],
                    created_at=created_at,
                )
            )

        return memories
