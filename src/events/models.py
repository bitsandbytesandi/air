from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


class ApplicationEventType(str, Enum):
    APPLICATION_STARTED = "application.started"
    APPLICATION_STOPPED = "application.stopped"

    CHAT_STARTED = "chat.started"
    CHAT_COMPLETED = "chat.completed"
    CHAT_FAILED = "chat.failed"

    MEMORY_CREATED = "memory.created"
    MEMORY_SEARCHED = "memory.searched"
    MEMORY_DELETED = "memory.deleted"

    TOOL_STARTED = "tool.started"
    TOOL_COMPLETED = "tool.completed"
    TOOL_FAILED = "tool.failed"

    SETTINGS_CHANGED = "settings.changed"


@dataclass(frozen=True)
class ApplicationEvent:
    event_type: ApplicationEventType
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    payload: dict[str, Any] = field(default_factory=dict)
