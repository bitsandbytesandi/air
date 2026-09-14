from core.application import ApplicationService
from core.errors import ApplicationError
from core.state import ApplicationState


class FakeChatService:
    def __init__(self):
        self.restore_count = 0

    def restore(self):
        self.restore_count += 1

    def get_messages(self):
        return []

    def chat(self, content, model, tokenizer, max_tokens=128):
        return f"Response: {content}"


fake_chat_service = FakeChatService()

application = ApplicationService(
    chat_service=fake_chat_service,
    model=None,
    tokenizer=None,
)


assert application.state == ApplicationState.CREATED

application.start()

assert application.state == ApplicationState.RUNNING
assert fake_chat_service.restore_count == 1

application.start()

assert application.state == ApplicationState.RUNNING
assert fake_chat_service.restore_count == 1

application.shutdown()

assert application.state == ApplicationState.STOPPED

try:
    application.chat("Hello")
    raise AssertionError(
        "Chat should not work after shutdown."
    )
except ApplicationError:
    pass


print("Brick 32 - Application lifecycle: GREEN")
