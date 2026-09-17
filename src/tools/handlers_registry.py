from collections.abc import Callable

from .handlers import ToolHandler


class ToolHandlerRegistry:
    def __init__(
        self,
        handlers: dict[str, ToolHandler] | None = None,
    ):
        self._handlers: dict[str, ToolHandler] = {}

        for tool_id, handler in (handlers or {}).items():
            self.register(
                tool_id,
                handler,
            )

    def register(
        self,
        tool_id: str,
        handler: ToolHandler,
    ) -> None:
        if tool_id in self._handlers:
            raise ValueError(
                f"Handler already registered: {tool_id}"
            )

        self._handlers[tool_id] = handler

    def get(
        self,
        tool_id: str,
    ) -> ToolHandler | None:
        return self._handlers.get(tool_id)
