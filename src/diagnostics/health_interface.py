from .health_collection import HealthCollection
from .runtime_health import RuntimeHealth
from .service_health import ServiceHealth
from .status import HealthStatus
from .system_health import SystemHealth


class HealthInterface:
    def __init__(
        self,
        collection: HealthCollection,
    ):
        self.collection = collection

    def get_system(self) -> SystemHealth | None:
        return self.collection.system()

    def get_runtime(self) -> RuntimeHealth | None:
        return self.collection.runtime()

    def get_services(self) -> list[ServiceHealth]:
        return self.collection.services()

    def get_status(self) -> HealthStatus:
        system = self.collection.system()

        if system is None:
            return HealthStatus.UNHEALTHY

        return system.status
