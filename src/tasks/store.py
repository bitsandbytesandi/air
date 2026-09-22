from .models import Task


class TaskStore:
    def __init__(self):
        self._tasks: dict[str, Task] = {}

    def save(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get(self, task_id: str) -> Task | None:
        return self._tasks.get(task_id)

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def delete(self, task_id: str) -> None:
        self._tasks.pop(task_id, None)
