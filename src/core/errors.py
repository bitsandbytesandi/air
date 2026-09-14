class ApplicationError(Exception):
    """Base error for application-level failures."""

class InvalidMessageError(ApplicationError):
    """Raised when a chat message is invalid."""
