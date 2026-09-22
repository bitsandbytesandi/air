from .manager import TaskManager
from .models import Task, TaskStatus


class TaskOperations:
    def __init__(self, manager: TaskManager):
        self.manager = manager

    def start(self, task_id: str) -> Task:
        return self.manager.transition(
            task_id,
            TaskStatus.RUNNING,
        )

    def complete(self, task_id: str) -> Task:
        return self.manager.transition(
            task_id,
            TaskStatus.COMPLETED,
        )

    def fail(self, task_id: str) -> Task:
        return self.manager.transition(
            task_id,
            TaskStatus.FAILED,
        )

    def cancel(self, task_id: str) -> Task:
        return self.manager.transition(
            task_id,
            TaskStatus.CANCELLED,
        )
