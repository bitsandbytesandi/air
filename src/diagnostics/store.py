from .errors import DiagnosticError
from .logs import DiagnosticLog
from .stats import ExecutionStats


class DiagnosticsStore:
    def __init__(self):
        self._logs: list[DiagnosticLog] = []
        self._errors: list[DiagnosticError] = []
        self._stats: dict[str, ExecutionStats] = {}

    def add_log(
        self,
        log: DiagnosticLog,
    ) -> None:
        self._logs.append(log)

    def add_error(
        self,
        error: DiagnosticError,
    ) -> None:
        self._errors.append(error)

    def set_stats(
        self,
        stats: ExecutionStats,
    ) -> None:
        self._stats[stats.tool_id] = stats

    def get_logs(self) -> list[DiagnosticLog]:
        return list(self._logs)

    def get_errors(self) -> list[DiagnosticError]:
        return list(self._errors)

    def get_stats(
        self,
        tool_id: str,
    ) -> ExecutionStats | None:
        return self._stats.get(tool_id)

    def get_all_stats(self) -> list[ExecutionStats]:
        return list(self._stats.values())
