from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4
from typing import Any


@dataclass
class Trace:
    trace_id: str
    operation: str
    started_at: datetime
    completed_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def start(
        cls,
        operation: str,
        metadata: dict[str, Any] | None = None,
    ) -> "Trace":
        return cls(
            trace_id=str(uuid4()),
            operation=operation,
            started_at=datetime.now(timezone.utc),
            metadata=metadata or {},
        )

    def complete(self) -> None:
        self.completed_at = datetime.now(timezone.utc)
