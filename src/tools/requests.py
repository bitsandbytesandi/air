from dataclasses import dataclass


@dataclass(frozen=True)
class ToolExecutionRequest:
    tool_id: str
    arguments: dict
