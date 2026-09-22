from .models import ToolInvocation
from .factory import InvocationFactory

class OrchestrationService:
    """Coordinates creation of tool invocations."""

    def __init__(self, factory: InvocationFactory):
        self.factory = factory

    def create_invocation(
        self,
        task_id: str,
        tool_id: str,
        arguments: dict,
    ) -> ToolInvocation:
        return self.factory.create(
            task_id=task_id,
            tool_id=tool_id,
            arguments=arguments,
        )
