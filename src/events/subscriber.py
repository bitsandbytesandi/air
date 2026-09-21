from .models import ApplicationEvent


class EventSubscriber:
    def handle(
        self,
        event: ApplicationEvent,
    ) -> None:
        raise NotImplementedError
