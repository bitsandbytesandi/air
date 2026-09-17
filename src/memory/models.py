from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class Memory:
    id: UUID
    content: str
    created_at: datetime

    @classmethod
    def create(
        cls,
        content: str,
    ) -> "Memory":
        return cls(
            id=uuid4(),
            content=content,
            created_at=datetime.now(),
        )
