from .discovery import ToolDiscovery
from .models import Tool


class ToolService:
    def __init__(
        self,
        discovery: ToolDiscovery,
    ):
        self.discovery = discovery

    def available_tools(self) -> list[Tool]:
        return self.discovery.available_tools()
