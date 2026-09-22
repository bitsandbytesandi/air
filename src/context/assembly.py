from .collection import ContextCollection
from .provider import ContextProvider


class ContextAssembly:
    """Collects context items from registered providers."""

    def assemble(
        self,
        providers: list[ContextProvider],
    ) -> ContextCollection:
        collection = ContextCollection()

        for provider in providers:
            for item in provider.provide():
                collection.add(item)

        return collection
