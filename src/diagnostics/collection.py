from .errors import DiagnosticError
from .logs import DiagnosticLog
from .stats import ExecutionStats
from .store import DiagnosticsStore


class DiagnosticsCollection:
    def __init__(
        self,
        store: DiagnosticsStore,
    ):
        self.store = store

    def logs(self) -> list[DiagnosticLog]:
        return self.store.get_logs()

    def errors(self) -> list[DiagnosticError]:
        return self.store.get_errors()

    def stats(self) -> list[ExecutionStats]:
        return self.store.get_all_stats()
