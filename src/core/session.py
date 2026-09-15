from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

@dataclass
class Session:
    id: str
    started_at: datetime
    ended_at: datetime | None = None

    @classmethod
    def create(cls) -> "Session":
        return cls(
            id=str(uuid4()),
            started_at=datetime.now(timezone.utc),
        )

    @property
    def active(self) -> bool:
        return self.ended_at is None

    def close(self) -> None:
        if self.ended_at is not None:
            return

        self.ended_at = datetime.now(timezone.utc)
