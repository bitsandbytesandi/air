from dataclasses import dataclass
from enum import Enum


class FailureKind(str, Enum):
    TRANSIENT = "transient"
    PERMANENT = "permanent"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Failure:
    kind: FailureKind
    message: str
    operation: str


@dataclass(frozen=True)
class RecoveryResult:
    recovered: bool
    attempts: int
    failure: Failure | None = None
