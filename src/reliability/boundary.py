from collections.abc import Callable
from typing import TypeVar

from .events import RecoveryEvent, RecoveryEventFactory
from .models import RecoveryResult
from .observability import RecoveryObservation, RecoveryObserver
from .service import RecoveryService


T = TypeVar("T")


class RecoveryBoundary:
    def __init__(
        self,
        service: RecoveryService | None = None,
        event_factory: RecoveryEventFactory | None = None,
        observer: RecoveryObserver | None = None,
    ) -> None:
        self._service = service or RecoveryService()
        self._event_factory = (
            event_factory or RecoveryEventFactory()
        )
        self._observer = observer or RecoveryObserver()

    def execute(
        self,
        operation: Callable[[], T],
        operation_name: str,
    ) -> tuple[
        T | None,
        RecoveryResult,
        RecoveryEvent,
        RecoveryObservation,
    ]:
        result, recovery = self._service.execute(
            operation,
            operation_name,
        )

        event = self._event_factory.create(
            recovery,
            operation_name,
        )

        observation = self._observer.observe(
            event,
        )

        return (
            result,
            recovery,
            event,
            observation,
        )
