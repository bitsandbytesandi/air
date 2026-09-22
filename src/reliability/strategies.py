from abc import ABC, abstractmethod

from .models import Failure, FailureKind


class RecoveryStrategy(ABC):
    @abstractmethod
    def supports(self, failure: Failure) -> bool:
        raise NotImplementedError

    @abstractmethod
    def should_retry(self, failure: Failure) -> bool:
        raise NotImplementedError


class TransientRecoveryStrategy(RecoveryStrategy):
    def supports(self, failure: Failure) -> bool:
        return failure.kind is FailureKind.TRANSIENT

    def should_retry(self, failure: Failure) -> bool:
        return True


class TimeoutRecoveryStrategy(RecoveryStrategy):
    def supports(self, failure: Failure) -> bool:
        return failure.kind is FailureKind.TIMEOUT

    def should_retry(self, failure: Failure) -> bool:
        return True


class PermanentRecoveryStrategy(RecoveryStrategy):
    def supports(self, failure: Failure) -> bool:
        return failure.kind is FailureKind.PERMANENT

    def should_retry(self, failure: Failure) -> bool:
        return False


class CancelledRecoveryStrategy(RecoveryStrategy):
    def supports(self, failure: Failure) -> bool:
        return failure.kind is FailureKind.CANCELLED

    def should_retry(self, failure: Failure) -> bool:
        return False


class UnknownRecoveryStrategy(RecoveryStrategy):
    def supports(self, failure: Failure) -> bool:
        return failure.kind is FailureKind.UNKNOWN

    def should_retry(self, failure: Failure) -> bool:
        return False
