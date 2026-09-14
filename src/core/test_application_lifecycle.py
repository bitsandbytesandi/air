from datetime import datetime

from core.application import ApplicationService
from core.results import ChatResult


class FakeMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
        self.created_at = datetime.now()


class FakeChatService:
    def __init__(self):
        self.restore_count = 0
        self.chat_count = 0
        self.messages = []

    def restore(self):
        self.restore_count += 1

    def chat(self, content, model, tokenizer, max_tokens=128):
        self.chat_count += 1

        self.messages.append(
            FakeMessage("user", content)
        )

        self.messages.append(
            FakeMessage(
                "assistant",
                f"Fake response to: {content}",
            )
        )

        return f"Fake response to: {content}"

    def get_messages(self):
        return list(self.messages)


fake_chat_service = FakeChatService()

application = ApplicationService(
    chat_service=fake_chat_service,
    model=None,
    tokenizer=None,
)


# 1. Application starts
application.start()

assert fake_chat_service.restore_count == 1


# 2. Application starts again
application.start()

assert fake_chat_service.restore_count == 1


# 3. Send a message
result = application.chat("Hello AIR")

assert isinstance(result, ChatResult)
assert result.content == "Fake response to: Hello AIR"


# 4. Verify chat happened once
assert fake_chat_service.chat_count == 1


# 5. Verify conversation contains both sides
conversation = application.get_conversation()

assert len(conversation) == 2

assert conversation[0]["role"] == "user"
assert conversation[0]["content"] == "Hello AIR"

assert conversation[1]["role"] == "assistant"
assert conversation[1]["content"] == "Fake response to: Hello AIR"


# 6. Verify empty messages are rejected
try:
    application.chat("   ")
    raise AssertionError(
        "Empty message should have been rejected."
    )
except Exception as error:
    from core.errors import InvalidMessageError

    assert isinstance(error, InvalidMessageError)


print("Application lifecycle test: GREEN")
