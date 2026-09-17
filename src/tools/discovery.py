from .models import Tool
from .registry import ToolRegistry


class ToolDiscovery:
    def __init__(
        self,
        registry: ToolRegistry,
    ):
        self.registry = registry

    def available_tools(self) -> list[Tool]:
        return self.registry.all()

