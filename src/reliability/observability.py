from dataclasses import dataclass

from .events import RecoveryEvent


@dataclass(frozen=True)
class RecoveryObservation:
    operation: str
    event_type: str
    attempts: int


class RecoveryObserver:
    def observe(
        self,
        event: RecoveryEvent,
    ) -> RecoveryObservation:
        return RecoveryObservation(
            operation=event.operation,
            event_type=event.event_type,
            attempts=event.attempts,
        )
