from memory.service import MemoryService


class MemorySearchHandler:
    def __init__(
        self,
        memory_service: MemoryService,
    ):
        self.memory_service = memory_service

    def __call__(
        self,
        arguments: dict,
    ) -> object:
        query = arguments["query"]

        return self.memory_service.search(
            query
        )
