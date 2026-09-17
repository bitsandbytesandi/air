from collections.abc import Callable

from .models import Tool
from .results import ToolExecutionResult
from .validation import ToolArgumentValidator


class DefaultToolExecutor:
    def __init__(
        self,
        handlers: dict[str, Callable[[dict], object]],
        validator: ToolArgumentValidator | None = None,
    ):
        self.handlers = handlers
        self.validator = validator or ToolArgumentValidator()

    def execute(
        self,
        tool: Tool,
        arguments: dict,
    ) -> ToolExecutionResult:
        try:
            self.validator.validate(tool, arguments)

            handler = self.handlers.get(tool.id)

            if handler is None:
                return ToolExecutionResult(
                    tool_id=tool.id,
                    success=False,
                    error=f"No handler registered for tool: {tool.id}",
                )

            output = handler(arguments)

            return ToolExecutionResult(
                tool_id=tool.id,
                success=True,
                output=output,
            )

        except Exception as exc:
            return ToolExecutionResult(
                tool_id=tool.id,
                success=False,
                error=str(exc),
            )
