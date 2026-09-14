from core.application import ApplicationService
from core.commands import ChatCommand
from core.context import ApplicationContext
from core.results import ChatResult
from core.state import ApplicationState


class FakeChatService:
    def __init__(self):
        self.restore_count = 0
        self.chat_count = 0

    def restore(self):
        self.restore_count += 1

    def get_messages(self):
        return []

    def chat(self, content, model, tokenizer, max_tokens=128):
        self.chat_count += 1

        return (
            f"Fake response to '{content}' "
            f"with max_tokens={max_tokens}"
        )


fake_chat_service = FakeChatService()


context = ApplicationContext(
    chat_service=fake_chat_service,
    model=None,
    tokenizer=None,
)


application = ApplicationService(
    chat_service=context.chat_service,
    model=context.model,
    tokenizer=context.tokenizer,
)


# SYSTEM START
assert application.state == ApplicationState.CREATED

application.start()

assert application.state == ApplicationState.RUNNING
assert fake_chat_service.restore_count == 1


# COMMAND
command = ChatCommand(
    content="Hello AIR",
    max_tokens=64,
)


# EXECUTION
result = application.chat(
    command.content,
    max_tokens=command.max_tokens,
)


# RESULT
assert isinstance(result, ChatResult)

assert result.content == (
    "Fake response to 'Hello AIR' "
    "with max_tokens=64"
)

assert fake_chat_service.chat_count == 1


# SYSTEM SHUTDOWN
application.shutdown()

assert application.state == ApplicationState.STOPPED


print("Brick 35 - System integration: GREEN")
