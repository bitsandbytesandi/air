from tools.results import ToolExecutionResult

from .models import ToolInvocation
from .results import OrchestrationResult


class ResultMapper:
    """Maps tool execution results into orchestration results."""

    def map(
        self,
        invocation: ToolInvocation,
        execution_result: ToolExecutionResult,
    ) -> OrchestrationResult:
        return OrchestrationResult(
            task_id=invocation.task_id,
            tool_id=invocation.tool_id,
            success=execution_result.success,
            result=execution_result.output,
            error=execution_result.error,
        )
