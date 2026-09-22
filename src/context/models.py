from dataclasses import dataclass


@dataclass(frozen=True)
class ContextItem:
    """Represents one piece of information available to the context layer."""

    source: str
    content: str
