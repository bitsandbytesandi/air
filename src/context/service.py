from .assembly import ContextAssembly
from .collection import ContextCollection
from .provider import ContextProvider


class ContextService:
    """Application-facing service for context assembly."""

    def __init__(self, assembly: ContextAssembly):
        self.assembly = assembly

    def build(
        self,
        providers: list[ContextProvider],
    ) -> ContextCollection:
        return self.assembly.assemble(providers)
