from dataclasses import dataclass


@dataclass(frozen=True)
class ToolExecutionResult:
    tool_id: str
    success: bool
    output: object | None = None
    error: str | None = None
