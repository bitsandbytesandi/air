from dataclasses import dataclass


@dataclass(frozen=True)
class ToolInvocation:
    task_id: str
    tool_id: str
    arguments: dict
