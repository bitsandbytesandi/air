from .discovery import ToolDiscovery
from .execution_service import ToolExecutionService
from .models import Tool
from .requests import ToolExecutionRequest
from .results import ToolExecutionResult


class ToolService:
    def __init__(
        self,
        discovery: ToolDiscovery,
        execution: ToolExecutionService,
    ):
        self.discovery = discovery
        self.execution = execution

    def available_tools(self) -> list[Tool]:
        return self.discovery.available_tools()

    def execute(
        self,
        tool: Tool,
        request: ToolExecutionRequest,
    ) -> ToolExecutionResult:
        return self.execution.execute(
            tool,
            request,
        )
