from memory.service import MemoryService

from .definitions import MEMORY_SEARCH_TOOL
from .execution_service import ToolExecutionService
from .executor import DefaultToolExecutor
from .handlers_registry import ToolHandlerRegistry
from .memory_search import MemorySearchHandler
from .registry import create_default_registry
from .router import ToolExecutionRouter
from .service import ToolService


def create_tool_service(
    memory_service: MemoryService,
) -> ToolService:
    handler_registry = ToolHandlerRegistry()

    handler_registry.register(
        MEMORY_SEARCH_TOOL.id,
        MemorySearchHandler(
            memory_service
        ),
    )

    executor = DefaultToolExecutor(
        handlers={
            MEMORY_SEARCH_TOOL.id: handler_registry.get(
                MEMORY_SEARCH_TOOL.id
            ),
        }
    )

    router = ToolExecutionRouter(
        executor
    )

    execution_service = ToolExecutionService(
        router
    )

    registry = create_default_registry()

    from .discovery import ToolDiscovery

    discovery = ToolDiscovery(
        registry
    )

    return ToolService(
        discovery=discovery,
        execution=execution_service,
    )
