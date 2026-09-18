from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class DiagnosticEventType(str, Enum):
    LOG = "log"
    ERROR = "error"
    EXECUTION = "execution"


@dataclass(frozen=True)
class DiagnosticEvent:
    event_type: DiagnosticEventType
    timestamp: datetime
