from .errors import DiagnosticError
from .logs import DiagnosticLog
from .stats import ExecutionStats
from .store import DiagnosticsStore


class DiagnosticsService:
    def __init__(
        self,
        store: DiagnosticsStore,
    ):
        self.store = store

    def record_log(
        self,
        log: DiagnosticLog,
    ) -> None:
        self.store.add_log(log)

    def record_error(
        self,
        error: DiagnosticError,
    ) -> None:
        self.store.add_error(error)

    def record_stats(
        self,
        stats: ExecutionStats,
    ) -> None:
        self.store.set_stats(stats)
