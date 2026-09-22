from datetime import datetime, timezone

from .events import RuntimeEvent


class RuntimeEventFactory:
    """Creates runtime events with UTC timestamps."""

    def create(
        self,
        event_type: str,
        data: object | None = None,
    ) -> RuntimeEvent:
        return RuntimeEvent(
            event_type=event_type,
            timestamp=datetime.now(timezone.utc),
            data=data,
        )
