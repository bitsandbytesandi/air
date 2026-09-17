from .results import ToolExecutionResult
from .status import ToolExecution, ToolExecutionStatus


class ToolExecutionLifecycle:
    def start(
        self,
        tool_id: str,
    ) -> ToolExecution:
        return ToolExecution(
            tool_id=tool_id,
            status=ToolExecutionStatus.RUNNING,
        )

    def complete(
        self,
        execution: ToolExecution,
    ) -> ToolExecution:
        return ToolExecution(
            tool_id=execution.tool_id,
            status=ToolExecutionStatus.COMPLETED,
        )

    def fail(
        self,
        execution: ToolExecution,
    ) -> ToolExecution:
        return ToolExecution(
            tool_id=execution.tool_id,
            status=ToolExecutionStatus.FAILED,
        )
