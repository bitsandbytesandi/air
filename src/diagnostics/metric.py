from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class Metric:
    name: str
    value: float
    timestamp: datetime
    labels: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        name: str,
        value: float,
        labels: dict[str, Any] | None = None,
    ) -> "Metric":
        return cls(
            name=name,
            value=float(value),
            timestamp=datetime.now(timezone.utc),
            labels=labels or {},
        )
