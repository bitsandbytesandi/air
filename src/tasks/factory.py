from datetime import datetime, timezone
from uuid import uuid4

from .models import Task, TaskStatus


class TaskFactory:
    def create(
        self,
        task_type: str,
        metadata: dict | None = None,
    ) -> Task:
        return Task(
            id=f"task-{uuid4().hex}",
            task_type=task_type,
            status=TaskStatus.CREATED,
            created_at=datetime.now(timezone.utc),
            metadata=metadata or {},
        )
