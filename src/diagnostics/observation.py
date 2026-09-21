from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Observation:
    name: str
    timestamp: datetime
    payload: dict[str, Any]

    @classmethod
    def create(
        cls,
        name: str,
        payload: dict[str, Any] | None = None,
    ) -> "Observation":
        return cls(
            name=name,
            timestamp=datetime.now(timezone.utc),
            payload=payload or {},
        )
