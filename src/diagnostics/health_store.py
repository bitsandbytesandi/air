from .runtime_health import RuntimeHealth
from .service_health import ServiceHealth
from .system_health import SystemHealth


class HealthStore:
    def __init__(self):
        self._system: SystemHealth | None = None
        self._runtime: RuntimeHealth | None = None
        self._services: dict[str, ServiceHealth] = {}

    def set_system(
        self,
        health: SystemHealth,
    ) -> None:
        self._system = health

    def set_runtime(
        self,
        health: RuntimeHealth,
    ) -> None:
        self._runtime = health

    def set_service(
        self,
        health: ServiceHealth,
    ) -> None:
        self._services[health.service_name] = health

    def get_system(self) -> SystemHealth | None:
        return self._system

    def get_runtime(self) -> RuntimeHealth | None:
        return self._runtime

    def get_service(
        self,
        service_name: str,
    ) -> ServiceHealth | None:
        return self._services.get(service_name)

    def get_services(self) -> list[ServiceHealth]:
        return list(self._services.values())
