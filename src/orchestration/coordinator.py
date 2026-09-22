from tools.requests import ToolExecutionRequest

from .models import ToolInvocation
from .request_builder import InvocationRequestBuilder
from .service import OrchestrationService


class InvocationCoordinator:
    """Coordinates creation and translation of tool invocations."""

    def __init__(
        self,
        orchestration_service: OrchestrationService,
        request_builder: InvocationRequestBuilder,
    ):
        self.orchestration_service = orchestration_service
        self.request_builder = request_builder

    def prepare(
        self,
        task_id: str,
        tool_id: str,
        arguments: dict,
    ) -> tuple[ToolInvocation, ToolExecutionRequest]:
        invocation = self.orchestration_service.create_invocation(
            task_id=task_id,
            tool_id=tool_id,
            arguments=arguments,
        )

        request = self.request_builder.build(invocation)

        return invocation, request
