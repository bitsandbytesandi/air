from dataclasses import dataclass
from datetime import datetime, timezone

from .models import Failure, RecoveryResult


@dataclass(frozen=True)
class RecoveryEvent:
    operation: str
    event_type: str
    timestamp: datetime
    attempts: int
    failure: Failure | None = None


class RecoveryEventFactory:
    def create(
        self,
        result: RecoveryResult,
        operation: str,
    ) -> RecoveryEvent:
        if result.recovered:
            event_type = "recovery_succeeded"
        else:
            event_type = "recovery_failed"

        return RecoveryEvent(
            operation=operation,
            event_type=event_type,
            timestamp=datetime.now(timezone.utc),
            attempts=result.attempts,
            failure=result.failure,
        )
