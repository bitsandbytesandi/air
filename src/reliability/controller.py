from collections.abc import Callable
from typing import TypeVar

from .models import (
    Failure,
    FailureKind,
    RecoveryResult,
)
from .retry import RetryPolicy


T = TypeVar("T")


class RecoveryController:
    def __init__(
        self,
        policy: RetryPolicy | None = None,
    ) -> None:
        self._policy = policy or RetryPolicy()

    def execute(
        self,
        operation: Callable[[], T],
        operation_name: str,
    ) -> tuple[T | None, RecoveryResult]:
        attempts = 0

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

            except TimeoutError as exc:
                failure = Failure(
                    kind=FailureKind.TIMEOUT,
                    message=str(exc),
                    operation=operation_name,
                )

            except RuntimeError as exc:
                failure = Failure(
                    kind=FailureKind.TRANSIENT,
                    message=str(exc),
                    operation=operation_name,
                )

            except Exception as exc:
                failure = Failure(
                    kind=FailureKind.UNKNOWN,
                    message=str(exc),
                    operation=operation_name,
                )

        return (
            None,
            RecoveryResult(
                recovered=False,
                attempts=attempts,
                failure=failure,
            ),
        )
