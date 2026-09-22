from collections.abc import Callable
from typing import TypeVar

from .classifier import FailureClassifier
from .models import RecoveryResult
from .retry import RetryPolicy
from .strategies import (
    CancelledRecoveryStrategy,
    PermanentRecoveryStrategy,
    RecoveryStrategy,
    TimeoutRecoveryStrategy,
    TransientRecoveryStrategy,
    UnknownRecoveryStrategy,
)


T = TypeVar("T")


class RecoveryService:
    def __init__(
        self,
        policy: RetryPolicy | None = None,
        classifier: FailureClassifier | None = None,
        strategies: list[RecoveryStrategy] | None = None,
    ) -> None:
        self._policy = policy or RetryPolicy()
        self._classifier = classifier or FailureClassifier()

        self._strategies = strategies or [
            TransientRecoveryStrategy(),
            TimeoutRecoveryStrategy(),
            PermanentRecoveryStrategy(),
            CancelledRecoveryStrategy(),
            UnknownRecoveryStrategy(),
        ]

    def execute(
        self,
        operation: Callable[[], T],
        operation_name: str,
    ) -> tuple[T | None, RecoveryResult]:
        attempts = 0
        last_failure = None

        while self._policy.should_retry(attempts):
            attempts += 1

            try:
                result = operation()

                return (
                    result,
                    RecoveryResult(
                        recovered=True,
                        attempts=attempts,
                    ),
                )

            except Exception as exc:
                failure = self._classifier.classify(
                    exc,
                    operation_name,
                )

                last_failure = failure

                strategy = next(
                    (
                        candidate
                        for candidate in self._strategies
                        if candidate.supports(failure)
                    ),
                    None,
                )

                if strategy is None or not strategy.should_retry(
                    failure
                ):
                    break

        return (
            None,
            RecoveryResult(
                recovered=False,
                attempts=attempts,
                failure=last_failure,
            ),
        )
