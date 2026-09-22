from tools.models import Tool
from tools.results import ToolExecutionResult

from .execution import InvocationExecutionBoundary
from .models import ToolInvocation


class OrchestrationExecutionService:
    """Coordinates execution of tool invocations."""

    def __init__(
        self,
        execution_boundary: InvocationExecutionBoundary,
    ):
        self.execution_boundary = execution_boundary

    def execute(
        self,
        tool: Tool,
        invocation: ToolInvocation,
    ) -> ToolExecutionResult:
        return self.execution_boundary.execute(
            tool=tool,
            invocation=invocation,
        )
