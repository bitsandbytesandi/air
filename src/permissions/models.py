from dataclasses import dataclass

@dataclass(frozen=True)
class Permission:
    subject: str
    resource: str
    action: str
