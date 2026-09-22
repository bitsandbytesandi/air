from dataclasses import dataclass, field

from .types import PermissionAction, PermissionDecision


@dataclass(frozen=True)
class SafetyPolicy:
    default_decision: PermissionDecision = PermissionDecision.DENY
    allowed_actions: frozenset[PermissionAction] = field(
        default_factory=frozenset
    )
    denied_actions: frozenset[PermissionAction] = field(
        default_factory=frozenset
    )
