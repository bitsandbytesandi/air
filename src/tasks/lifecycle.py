from .models import TaskStatus


_ALLOWED_TRANSITIONS: dict[TaskStatus, frozenset[TaskStatus]] = {
    TaskStatus.CREATED: frozenset({
        TaskStatus.RUNNING,
        TaskStatus.CANCELLED,
    }),
    TaskStatus.RUNNING: frozenset({
        TaskStatus.COMPLETED,
        TaskStatus.FAILED,
        TaskStatus.CANCELLED,
    }),
    TaskStatus.COMPLETED: frozenset(),
    TaskStatus.FAILED: frozenset(),
    TaskStatus.CANCELLED: frozenset(),
}


def can_transition(
    current: TaskStatus,
    target: TaskStatus,
) -> bool:
    return target in _ALLOWED_TRANSITIONS[current]
