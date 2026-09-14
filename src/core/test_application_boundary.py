from datetime import datetime

from core.application import ApplicationService
from core.errors import InvalidMessageError
from core.results import ChatResult

class FakeMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
        self.created_at = datetime.now()


class FakeChatService:
    def __init__(self):
        self.restore_count = 0

    def get_messages(self):

        return [
            FakeMessage("user", "Hello AIR"),
            FakeMessage("assistant", "Hello! How can I help?"),
        ]

    def restore(self):
        self.restore_count += 1

    def chat(self, content, model, tokenizer, max_tokens=128):
        return f"Fake response to: {content}"


fake_chat_service = FakeChatService()

application = ApplicationService(
    chat_service=fake_chat_service,
    model=None,
    tokenizer=None,
)
application.start()
application.start()

assert fake_chat_service.restore_count == 1

conversation = application.get_conversation()

assert len(conversation) == 2
assert conversation[0]["role"] == "user"
assert conversation[0]["content"] == "Hello AIR"
assert conversation[1]["role"] == "assistant"


response = application.chat("Hello")

assert isinstance(response, ChatResult)
assert response.content == "Fake response to: Hello"


try:
    application.chat("   ")
    raise AssertionError("Empty message should have been rejected.")
except InvalidMessageError:
    pass


print("Application boundary test: GREEN")
