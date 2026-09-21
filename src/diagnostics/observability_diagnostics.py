from .errors import DiagnosticError
from .logs import DiagnosticLog
from .service import DiagnosticsService
from .stats import ExecutionStats


class ObservabilityDiagnostics:
    def __init__(
        self,
        diagnostics: DiagnosticsService,
    ):
        self.diagnostics = diagnostics

    def record_log(
        self,
        message: str,
        timestamp,
    ) -> None:
        self.diagnostics.record_log(
            DiagnosticLog(
                message=message,
                timestamp=timestamp,
            )
        )

    def record_error(
        self,
        message: str,
        timestamp,
        source: str | None = None,
    ) -> None:
        self.diagnostics.record_error(
            DiagnosticError(
                message=message,
                timestamp=timestamp,
                source=source,
            )
        )

    def record_stats(
        self,
        tool_id: str,
        executions: int = 0,
        successes: int = 0,
        failures: int = 0,
        total_duration_ms: float = 0.0,
    ) -> None:
        self.diagnostics.record_stats(
            ExecutionStats(
                tool_id=tool_id,
                executions=executions,
                successes=successes,
                failures=failures,
                total_duration_ms=total_duration_ms,
            )
        )
