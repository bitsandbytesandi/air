from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class RuntimeEvent:
    """Represents one event produced during runtime execution."""

    event_type: str
    timestamp: datetime
    data: object | None = None
