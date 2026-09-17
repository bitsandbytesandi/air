class ToolExecutionError(Exception):
    """Base error for tool execution."""


class ToolNotFoundError(ToolExecutionError):
    """Raised when a requested tool does not exist."""


class ToolValidationError(ToolExecutionError):
    """Raised when tool arguments are invalid."""


class ToolHandlerError(ToolExecutionError):
    """Raised when a tool handler fails."""
