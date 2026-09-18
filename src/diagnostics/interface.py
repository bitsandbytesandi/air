from .collection import DiagnosticsCollection
from .errors import DiagnosticError
from .logs import DiagnosticLog
from .stats import ExecutionStats


class DiagnosticsInterface:
    def __init__(
        self,
        collection: DiagnosticsCollection,
    ):
        self.collection = collection

    def get_logs(self) -> list[DiagnosticLog]:
        return self.collection.logs()

    def get_errors(self) -> list[DiagnosticError]:
        return self.collection.errors()

    def get_stats(self) -> list[ExecutionStats]:
        return self.collection.stats()
