from typing import Protocol

from .models import Tool


class ToolExecutor(Protocol):
    def execute(
        self,
        tool: Tool,
        arguments: dict,
    ) -> object:
        ...
