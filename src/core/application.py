from collections.abc import Iterator

from core.context import ApplicationContext
from core.errors import ApplicationError, InvalidMessageError
from core.results import ChatResult
from core.state import ApplicationState
from integration.boundary import AIRIntegration


class ApplicationService:

    def __init__(
        self,
        context: ApplicationContext,
        integration: AIRIntegration,
    ):
        self.context = context
        self.integration = integration
        self._state = ApplicationState.CREATED

    @property
    def state(self) -> ApplicationState:
        return self._state

    @property
    def session(self):
        return self.context.session

    def start(self) -> None:
        if self._state == ApplicationState.RUNNING:
            return

        if self._state == ApplicationState.STOPPING:
            raise ApplicationError(
                "Application is stopping."
            )

        self._state = ApplicationState.STARTING

        try:
            self.restore()
            self._state = ApplicationState.RUNNING
        except Exception:
            self._state = ApplicationState.FAILED
            raise

    def delete_memory(
        self,
        memory_id,
    ) -> bool:
        if self._state != ApplicationState.RUNNING:
            raise ApplicationError(
                "Application is not running."
            )

        return self.context.memory_service.delete(
            memory_id
        )

    def shutdown(self) -> None:
        if self._state == ApplicationState.STOPPED:
            return

        if self._state != ApplicationState.RUNNING:
            return

        self._state = ApplicationState.STOPPING
        self.context.session.close()
        self._state = ApplicationState.STOPPED

    def _validate_chat(
        self,
        content: str,
    ) -> str:
        if self._state != ApplicationState.RUNNING:
            raise ApplicationError(
                "Application is not running."
            )

        content = content.strip()

        if not content:
            raise InvalidMessageError(
                "Message cannot be empty."
            )

        return content

    def chat(
        self,
        content: str,
        max_tokens: int | None = None,
    ) -> ChatResult:
        content = self._validate_chat(content)

        resolved_max_tokens = (
            max_tokens
            if max_tokens is not None
            else self.context.runtime.max_tokens
        )

        response = self.context.chat_service.chat(
            content,
            self.context.model,
            self.context.tokenizer,
            max_tokens=resolved_max_tokens,
        )

        return ChatResult(
            content=response,
        )

    def get_tool_service(self):
        return self.context.tool_service

    def stream_chat(
        self,
        content: str,
        max_tokens: int | None = None,
    ) -> Iterator[str]:
        content = self._validate_chat(content)

        resolved_max_tokens = (
            max_tokens
            if max_tokens is not None
            else self.context.runtime.max_tokens
        )

        yield from self.context.chat_service.stream_chat(
            content,
            self.context.model,
            self.context.tokenizer,
            max_tokens=resolved_max_tokens,
        )

    def get_messages(self):
        return self.context.chat_service.get_messages()

    def get_conversation(self) -> list[dict[str, str]]:
        messages = self.context.chat_service.get_messages()

        return [
            {
                "role": message.role,
                "content": message.content,
                "created_at": message.created_at.isoformat(),
            }
            for message in messages
        ]

    def get_memories(self):
        return self.context.memory_service.get_all()

    def search_memories(
        self,
        query: str,
    ):
        if self._state != ApplicationState.RUNNING:
            raise ApplicationError(
                "Application is not running."
            )

        return self.context.memory_service.search(
            query
        )

    def remember(
        self,
        content: str,
    ):
        if self._state != ApplicationState.RUNNING:
            raise ApplicationError(
                "Application is not running."
            )

        content = content.strip()

        if not content:
            raise InvalidMessageError(
                "Memory cannot be empty."
            )

        return self.context.memory_service.remember(
            content
        )

    def restore(self) -> None:
        self.context.chat_service.restore()
        self.context.memory_service.restore()
