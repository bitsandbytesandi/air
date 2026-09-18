from dataclasses import dataclass

from .status import HealthStatus


@dataclass(frozen=True)
class ServiceHealth:
    service_name: str
    status: HealthStatus
