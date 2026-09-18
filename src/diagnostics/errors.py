from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DiagnosticError:
    message: str
    timestamp: datetime
    source: str | None = None
