from dataclasses import dataclass


@dataclass(frozen=True)
class RuntimeHealth:
    uptime_seconds: float
    healthy: bool
