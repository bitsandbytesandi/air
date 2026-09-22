from .models import Failure, FailureKind


class FailureClassifier:
    def classify(
        self,
        exception: Exception,
        operation: str,
    ) -> Failure:
        if isinstance(exception, TimeoutError):
            kind = FailureKind.TIMEOUT

        elif isinstance(exception, RuntimeError):
            kind = FailureKind.TRANSIENT

        elif isinstance(exception, KeyboardInterrupt):
            kind = FailureKind.CANCELLED

        else:
            kind = FailureKind.UNKNOWN

        return Failure(
            kind=kind,
            message=str(exception),
            operation=operation,
        )
