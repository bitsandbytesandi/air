from tools.execution_service import ToolExecutionService
from tools.models import Tool
from tools.results import ToolExecutionResult

from .request_builder import InvocationRequestBuilder
from .models import ToolInvocation


class InvocationExecutionBoundary:
    """Bridges orchestration invocations to the tool execution service."""

    def __init__(
        self,
        execution_service: ToolExecutionService,
        request_builder: InvocationRequestBuilder,
    ):
        self.execution_service = execution_service
        self.request_builder = request_builder

    def execute(
        self,
        tool: Tool,
        invocation: ToolInvocation,
    ) -> ToolExecutionResult:
        request = self.request_builder.build(invocation)

        return self.execution_service.execute(
            tool,
            request,
        )
