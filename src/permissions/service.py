from .models import Permission
from .policy import SafetyPolicy
from .types import PermissionAction, PermissionDecision


class AuthorizationService:
    def __init__(
        self,
        policy: SafetyPolicy,
    ):
        self.policy = policy

    def authorize(
        self,
        permission: Permission,
    ) -> PermissionDecision:
        try:
            action = PermissionAction(permission.action)
        except ValueError:
            return PermissionDecision.DENY

        if action in self.policy.denied_actions:
            return PermissionDecision.DENY

        if action in self.policy.allowed_actions:
            return PermissionDecision.ALLOW

        return self.policy.default_decision
