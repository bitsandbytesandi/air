from .health_store import HealthStore
from .runtime_health import RuntimeHealth
from .service_health import ServiceHealth
from .system_health import SystemHealth


class HealthCollection:
    def __init__(
        self,
        store: HealthStore,
    ):
        self.store = store

    def system(self) -> SystemHealth | None:
        return self.store.get_system()

    def runtime(self) -> RuntimeHealth | None:
        return self.store.get_runtime()

    def services(self) -> list[ServiceHealth]:
        return self.store.get_services()
