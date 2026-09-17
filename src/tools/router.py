from .executor import DefaultToolExecutor
from .models import Tool
from .requests import ToolExecutionRequest
from .results import ToolExecutionResult


class ToolExecutionRouter:
    def __init__(
        self,
        executor: DefaultToolExecutor,
    ):
        self.executor = executor

    def execute(
        self,
        tool: Tool,
        request: ToolExecutionRequest,
    ) -> ToolExecutionResult:
        if request.tool_id != tool.id:
            return ToolExecutionResult(
                tool_id=request.tool_id,
                success=False,
                error="Tool ID does not match execution request.",
            )

        return self.executor.execute(
            tool,
            request.arguments,
        )
