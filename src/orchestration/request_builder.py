from tools.requests import ToolExecutionRequest

from .models import ToolInvocation


class InvocationRequestBuilder:
    """Builds tool execution requests from orchestration invocations."""

    def build(self, invocation: ToolInvocation) -> ToolExecutionRequest:
        return ToolExecutionRequest(
            tool_id=invocation.tool_id,
            arguments=invocation.arguments,
        )
