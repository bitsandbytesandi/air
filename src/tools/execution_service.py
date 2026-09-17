from .models import Tool
from .requests import ToolExecutionRequest
from .results import ToolExecutionResult
from .router import ToolExecutionRouter


class ToolExecutionService:
    def __init__(
        self,
        router: ToolExecutionRouter,
    ):
        self.router = router

    def execute(
        self,
        tool: Tool,
        request: ToolExecutionRequest,
    ) -> ToolExecutionResult:
        return self.router.execute(
            tool,
            request,
        )
