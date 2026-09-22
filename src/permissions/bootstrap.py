from .policy import SafetyPolicy
from .service import AuthorizationService


def create_authorization_service() -> AuthorizationService:
    policy = SafetyPolicy()

    return AuthorizationService(
        policy
    )
