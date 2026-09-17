from dataclasses import dataclass
from enum import Enum


class ToolExecutionStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(frozen=True)
class ToolExecution:
    tool_id: str
    status: ToolExecutionStatus
