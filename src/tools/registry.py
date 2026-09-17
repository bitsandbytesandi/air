from .definitions import MEMORY_SEARCH_TOOL
from .models import Tool


class ToolRegistry:
    def __init__(
        self,
        tools: list[Tool] | None = None,
    ):
        self._tools = {}

        for tool in tools or []:
            self.register(tool)

    def register(
        self,
        tool: Tool,
    ) -> None:
        if tool.id in self._tools:
            raise ValueError(
                f"Tool already registered: {tool.id}"
            )

        self._tools[tool.id] = tool

    def get(
        self,
        tool_id: str,
    ) -> Tool | None:
        return self._tools.get(tool_id)

    def all(self) -> list[Tool]:
        return list(self._tools.values())


def create_default_registry() -> ToolRegistry:
    return ToolRegistry(
        tools=[
            MEMORY_SEARCH_TOOL,
        ]
    )

