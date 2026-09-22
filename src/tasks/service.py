from .factory import TaskFactory
from .manager import TaskManager
from .models import Task
from .operations import TaskOperations
from .store import TaskStore


class TaskService:
    def __init__(
        self,
        store: TaskStore,
        factory: TaskFactory | None = None,
    ):
        self.store = store
        self.factory = factory or TaskFactory()
        self.manager = TaskManager(store)
        self.operations = TaskOperations(self.manager)

    def create(
        self,
        task_type: str,
        metadata: dict | None = None,
    ) -> Task:
        task = self.factory.create(
            task_type=task_type,
            metadata=metadata,
        )
        self.store.save(task)
        return task

    def get(self, task_id: str) -> Task | None:
        return self.store.get(task_id)

    def list(self) -> list[Task]:
        return self.store.get_all()

    def delete(self, task_id: str) -> None:
        self.store.delete(task_id)

    def start(self, task_id: str) -> Task:
        return self.operations.start(task_id)

    def complete(self, task_id: str) -> Task:
        return self.operations.complete(task_id)

    def fail(self, task_id: str) -> Task:
        return self.operations.fail(task_id)

    def cancel(self, task_id: str) -> Task:
        return self.operations.cancel(task_id)
