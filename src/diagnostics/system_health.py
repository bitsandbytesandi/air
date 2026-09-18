from dataclasses import dataclass
from datetime import datetime

from .status import HealthStatus


@dataclass(frozen=True)
class SystemHealth:
    status: HealthStatus
    timestamp: datetime
