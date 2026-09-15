from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Session:
    id: str
    started_at: datetime

    @classmethod
    def create(cls) -> "Session":
        return cls(
            id=str(uuid4()),
            started_at=datetime.now(timezone.utc),
        )
