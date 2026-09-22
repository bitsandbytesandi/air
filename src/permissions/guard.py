from dataclasses import dataclass

from tools.models import Tool
from tools.requests import ToolExecutionRequest

from .models import Permission
from .service import AuthorizationService
from .types import PermissionAction, PermissionDecision


@dataclass(frozen=True)
class AuthorizationResult:
    decision: PermissionDecision
    tool_id: str


class ToolExecutionGuard:
    def __init__(
        self,
        authorization: AuthorizationService,
    ):
        self.authorization = authorization

    def authorize(
        self,
        tool: Tool,
        request: ToolExecutionRequest,
    ) -> AuthorizationResult:
        permission = Permission(
            subject="air",
            resource=tool.id,
            action=PermissionAction.EXECUTE.value,
        )

        decision = self.authorization.authorize(
            permission
        )

        return AuthorizationResult(
            decision=decision,
            tool_id=request.tool_id,
        )
