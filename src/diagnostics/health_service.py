from .health_store import HealthStore
from .runtime_health import RuntimeHealth
from .service_health import ServiceHealth
from .status import HealthStatus
from .system_health import SystemHealth


class HealthService:
    def __init__(
        self,
        store: HealthStore,
    ):
        self.store = store

    def record_system(
        self,
        health: SystemHealth,
    ) -> None:
        self.store.set_system(health)

    def record_runtime(
        self,
        health: RuntimeHealth,
    ) -> None:
        self.store.set_runtime(health)

    def record_service(
        self,
        health: ServiceHealth,
    ) -> None:
        self.store.set_service(health)

    def current_status(self) -> HealthStatus:
        system = self.store.get_system()

        if system is None:
            return HealthStatus.UNHEALTHY

        return system.status
