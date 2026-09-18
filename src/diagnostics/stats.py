from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionStats:
    tool_id: str
    executions: int = 0
    successes: int = 0
    failures: int = 0
    total_duration_ms: float = 0.0

    @property
    def average_duration_ms(self) -> float:
        if self.executions == 0:
            return 0.0

        return self.total_duration_ms / self.executions
