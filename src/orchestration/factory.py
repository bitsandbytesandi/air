from .models import ToolInvocation


class InvocationFactory:
    """Creates ToolInvocation instances for the orchestration layer."""

    def create(
        self,
        task_id: str,
        tool_id: str,
        arguments: dict,
    ) -> ToolInvocation:
        return ToolInvocation(
            task_id=task_id,
            tool_id=tool_id,
            arguments=arguments,
        )
