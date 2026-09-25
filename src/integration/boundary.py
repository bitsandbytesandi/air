from collections.abc import Callable
from typing import TypeVar

from .system import AIRSystem


T = TypeVar("T")


class AIRIntegration:
    """
    Integration boundary for the AIR application.

    This class coordinates existing subsystems without
    taking ownership of their internal responsibilities.
    """

    def __init__(self, system: AIRSystem) -> None:
        self._system = system

    @property
    def system(self) -> AIRSystem:
        return self._system

    def build_context(self):
        return self._system.context.build_snapshot()

    def execute_reliable(
        self,
        operation: Callable[[], T],
        operation_name: str,
    ):
        return self._system.reliability.execute(
            operation,
            operation_name,
        )

    @property
    def runtime(self):
        return self._system.runtime
