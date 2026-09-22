from dataclasses import dataclass


@dataclass(frozen=True)
class OrchestrationResult:
    """Represents the outcome of an orchestration operation."""

    task_id: str
    tool_id: str
    success: bool
    result: object | None = None
    error: str | None = None
