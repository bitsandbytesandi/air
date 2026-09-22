from dataclasses import dataclass

from .models import ContextItem


@dataclass(frozen=True)
class ContextSnapshot:
    """Immutable snapshot of assembled context."""

    items: tuple[ContextItem, ...]
