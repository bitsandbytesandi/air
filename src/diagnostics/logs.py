from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DiagnosticLog:
    message: str
    timestamp: datetime
