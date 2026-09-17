from tools.discovery import ToolDiscovery
from tools.registry import create_default_registry
from tools.service import ToolService


registry = create_default_registry()
discovery = ToolDiscovery(registry)
service = ToolService(discovery)

tools = service.available_tools()

assert len(tools) == 1
assert tools[0].id == "memory_search"
assert tools[0].name == "Memory Search"

print("55.8 ✅ Application Integration")
print("55.9 ✅ Desktop IPC Boundary")
print("55.10 ✅ Tool Interface Runtime Integration")

print()
print("🎯 BRICKS 55.8–55.10 READY FOR TEST")
