from .provider import ContextProvider


class ContextProviderCollection:
    """Stores context providers."""

    def __init__(self):
        self._providers: list[ContextProvider] = []

    def add(self, provider: ContextProvider) -> None:
        self._providers.append(provider)

    def get_all(self) -> list[ContextProvider]:
        return list(self._providers)
