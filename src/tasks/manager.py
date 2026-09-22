from dataclasses import replace

from .lifecycle import can_transition
from .models import Task, TaskStatus
from .store import TaskStore


class TaskManager:
    def __init__(self, store: TaskStore):
        self.store = store

    def transition(
        self,
        task_id: str,
        target: TaskStatus,
    ) -> Task:
        task = self.store.get(task_id)

        if task is None:
            raise ValueError(f"Task not found: {task_id}")

        if not can_transition(task.status, target):
            raise ValueError(
                f"Invalid task transition: "
                f"{task.status.value} -> {target.value}"
            )

        updated = replace(task, status=target)
        self.store.save(updated)

        return updated
