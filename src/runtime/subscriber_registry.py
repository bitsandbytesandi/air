from .subscriber import RuntimeEventSubscriber


class RuntimeSubscriberRegistry:
    """Stores registered runtime event subscribers."""

    def __init__(self):
        self._subscribers: list[RuntimeEventSubscriber] = []

    def register(self, subscriber: RuntimeEventSubscriber) -> None:
        self._subscribers.append(subscriber)

    def get_all(self) -> list[RuntimeEventSubscriber]:
        return list(self._subscribers)
